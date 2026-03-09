import json, re
from collections import Counter, defaultdict

# ✅ 너가 고정한 화이트리스트(반드시 너가 실제 사용한 리스트로 맞춰)
WHITELIST = set([
    "교통행정(주차/단속)",
    "도로관리(도로/보도/시설물)",
    "청소행정(폐기물/불법투기)",
    "환경관리(소음/진동/악취/빛공해)",
    "건축허가(인허가/불법건축)",
    "건설관리(국공유지/점용/노점)",
    "하수/치수(배수/침수/하수)",
    "공원녹지(공원/녹지/가로수)",
    "민원총괄(이첩/조정)",
    "재난안전(위험/안전조치)",
    "보건소 위생관리(식품/음식점/해충)",
    "보건소 건강증진(금연/흡연)",
    "경찰서(교통/치안)",
    "시청/광역(교통/버스/광역협의)",
    # 공단(너가 고정한 것만)
    "국민건강보험공단",
    "국민연금공단",
    "근로복지공단",
    "공무원연금공단",
    "한국장애인고용공단",
    "한국보훈복지의료공단",
    "도로교통공단",
    "한국승강기안전공단",
    "한국해양교통안전공단",
    "한국산업안전보건공단",
    "한국산업인력공단",
    "한국산업단지공단",
    "소상공인시장진흥공단",
    "중소벤처기업진흥공단",
    "한국환경공단",
    "해양환경공단",
    "한국법무보호복지공단",
    "가덕도신공항건설공단",
])

ALLOWED_STATUS = set(["accepted","supplement_requested","rejected","no_action","transferred","closed"])

def is_noisy(text: str) -> bool:
    # 대충 60~70% 노이즈 체크용 휴리스틱
    if re.search(r"[!?]{2,}", text): return True
    if re.search(r"[ㄱ-ㅎㅏ-ㅣ]{2,}", text): return True  # ㅋㅋ, ㅠㅠ, ㅇㅋ 같은
    if "해주새요" in text or "읍니다" in text or "안되요" in text or "소움" in text: return True
    if re.search(r"\S{12,}", text): return True  # 공백 거의 없는 긴 덩어리(길이막혀서...)
    return False

with open("merged_noisy.json","r",encoding="utf-8") as f:
    data = json.load(f)

print("N =", len(data))

# 1) 필수 키 존재/타입 검증
required_top = ["id","raw_citizen_input","complaint_type","location_text","jurisdiction_prediction",
                "missing_information_fields","supplement_request_probability","hidden_critical_defect","processing_outcome"]
bad = 0
for i,x in enumerate(data):
    for k in required_top:
        if k not in x:
            print("Missing key", k, "in", x.get("id"))
            bad += 1
            break

print("Missing-key rows:", bad)

# 2) 화이트리스트 검증 (후보/최종)
wl_viol = []
for x in data:
    cand = x["jurisdiction_prediction"]["candidates"]
    for c in cand:
        if c["department"] not in WHITELIST:
            wl_viol.append((x["id"], c["department"]))
    final_dep = x["processing_outcome"]["final_responsible_department"]
    if final_dep not in WHITELIST:
        wl_viol.append((x["id"], final_dep))

print("Whitelist violations:", len(wl_viol))
if wl_viol[:10]:
    print("Examples:", wl_viol[:10])

# 3) status 분포 / label 분포
status_cnt = Counter(x["processing_outcome"]["resolution_status"] for x in data)
dept_cnt = Counter(x["processing_outcome"]["final_responsible_department"] for x in data)
ctype_cnt = Counter(x["complaint_type"] for x in data)

print("\nStatus distribution:", status_cnt)
print("Top final departments:", dept_cnt.most_common(10))
print("Top complaint_type:", ctype_cnt.most_common(10))

# 4) high-conf wrong count
hcw = [x for x in data if x.get("confidence_score", -1) >= 0.85
       and x["processing_outcome"]["initial_routing_correct"] == False]
print("\nHigh-conf wrong:", len(hcw), f"({len(hcw)/len(data):.1%})")

# 5) supplement 확률 분포
sup_hi = [x for x in data if x["supplement_request_probability"]>=0.8]
sup_lo = [x for x in data if x["supplement_request_probability"]<=0.2]
print("Supplement >=0.8:", len(sup_hi), f"({len(sup_hi)/len(data):.1%})")
print("Supplement <=0.2:", len(sup_lo), f"({len(sup_lo)/len(data):.1%})")

# 6) 노이즈 비율(대략)
noisy = sum(1 for x in data if is_noisy(x["raw_citizen_input"]))
print("\nEstimated noise ratio:", noisy, "/", len(data), f"= {noisy/len(data):.1%}")

# 7) ID 중복/형식 감지 (이미 merge에서 중복은 막았지만 형식 확인)
fmt_bad = [x["id"] for x in data if not re.match(r"^HARD-2026-B\d{2}-\d{4}$", x["id"])]
print("Bad ID format:", len(fmt_bad))
if fmt_bad[:10]:
    print("Examples:", fmt_bad[:10])

# 8) status 값 검증
st_bad = [x["id"] for x in data if x["processing_outcome"]["resolution_status"] not in ALLOWED_STATUS]
print("Bad resolution_status:", len(st_bad))
if st_bad[:10]:
    print("Examples:", st_bad[:10])

# 9) missing confidence score
missing_cs = [x["id"] for x in data if "confidence_score" not in x]
print("Missing top-level confidence_score:", len(missing_cs))