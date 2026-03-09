import json, random, re
from pathlib import Path

random.seed(20260228)

IN_PATH = "merged.json"              # 입력
OUT_MERGED = "merged_noisy.json"     # 노이즈 반영 merged
OUT_DIR = Path("out")                # 산출물 폴더
OUT_DIR.mkdir(exist_ok=True)

# 노이즈 주입 확률(아이템 단위)
TARGET_NOISE_ITEM_RATIO = 0.50

# 노이즈 강도(적당히)
MAX_OPS_PER_ITEM = 3

# 너 validate.py의 heuristic에 잘 걸리게 만드는 "눈에 띄는" 노이즈 패턴들
COMMON_TYPO_MAP = {
    "안돼요": "안되요",
    "되나요": "되나여",
    "해주세요": "해주새요",
    "있습니다": "읍니다",
    "없습니다": "없슴니다",
    "소음": "소움",
    "처리": "처리요",
}

EMO_TOKENS = ["ㅠㅠ", "ㅜㅜ", "ㅋㅋ", "하..", "진짜", "아니", "와", "제발"]
PUNCS = ["!!", "???", "...."]

def add_repeated_punc(s: str) -> str:
    return s + random.choice(PUNCS)

def drop_some_spaces(s: str) -> str:
    # 임의로 공백 몇 개 제거(과도하지 않게)
    parts = s.split(" ")
    if len(parts) < 6:
        return s
    idxs = random.sample(range(1, len(parts)-1), k=min(2, len(parts)//8))
    for i in idxs:
        parts[i] = parts[i].replace(" ", "")
    # 일부 공백 제거 효과: 그냥 join에서 공백 수 줄이기
    out = []
    for i,p in enumerate(parts):
        if i in idxs:
            out.append(p)  # 앞뒤 공백 자연스럽게 줄어듦
        else:
            out.append(p)
    return " ".join(out)

def inject_typo(s: str) -> str:
    # 문장 내 일부 표현을 오타로 치환
    for k,v in COMMON_TYPO_MAP.items():
        if k in s and random.random() < 0.5:
            s = s.replace(k, v, 1)
            break
    return s

def add_emotion_token(s: str) -> str:
    tok = random.choice(EMO_TOKENS)
    # 문장 앞/중간에 끼워 넣기
    if random.random() < 0.6:
        return f"{tok} {s}"
    else:
        # 중간 삽입
        pos = max(1, min(len(s)-1, int(len(s)*random.uniform(0.2, 0.6))))
        return s[:pos] + f" {tok} " + s[pos:]

def fragment_sentence(s: str) -> str:
    # 문장 끝을 일부러 끊거나 말줄임
    if len(s) < 40:
        return s
    cut = int(len(s) * random.uniform(0.65, 0.9))
    return s[:cut].rstrip() + "…"

def apply_noise(s: str) -> str:
    ops = []
    # 노이즈 오퍼레이션 후보
    ops_pool = [inject_typo, add_emotion_token, drop_some_spaces, add_repeated_punc, fragment_sentence]
    k = random.randint(1, MAX_OPS_PER_ITEM)
    chosen = random.sample(ops_pool, k=k)
    for fn in chosen:
        s = fn(s)
    return s

def is_noisy_like_validate(text: str) -> bool:
    # 너 validate.py의 휴리스틱과 유사하게 측정(대략)
    if re.search(r"[!?]{2,}", text): return True
    if re.search(r"[ㄱ-ㅎㅏ-ㅣ]{2,}", text): return True
    if "해주새요" in text or "읍니다" in text or "안되요" in text or "소움" in text: return True
    if re.search(r"\S{12,}", text): return True
    return False

def dump_jsonl(items, path: Path):
    with path.open("w", encoding="utf-8") as f:
        for x in items:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")

with open(IN_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

n = len(data)
noise_targets = set(random.sample(range(n), k=int(n*TARGET_NOISE_ITEM_RATIO)))

for i,x in enumerate(data):
    if i in noise_targets:
        x["raw_citizen_input"] = apply_noise(x["raw_citizen_input"])

# 노이즈 비율 확인(heuristic)
noisy = sum(1 for x in data if is_noisy_like_validate(x["raw_citizen_input"]))
print(f"[NoiseCheck] estimated noisy ratio: {noisy}/{n} = {noisy/n:.1%}")

# 저장
with open(OUT_MERGED, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 2) Split: train/val/test + hard_test
random.shuffle(data)
n_train = int(n*0.8)
n_val = int(n*0.1)

train = data[:n_train]
val = data[n_train:n_train+n_val]
test = data[n_train+n_val:]

# Hard set: 고신뢰 오분류 + initial wrong 전체
hard = [x for x in data if (x.get("confidence_score", -1) >= 0.85 and x["processing_outcome"]["initial_routing_correct"] == False)]
# hard가 너무 작으면, initial wrong 전체를 더 포함
if len(hard) < 30:
    hard = [x for x in data if x["processing_outcome"]["initial_routing_correct"] == False]

print(f"[Split] train/val/test = {len(train)}/{len(val)}/{len(test)}")
print(f"[HardSet] hard size = {len(hard)}")

dump_jsonl(train, OUT_DIR/"train.jsonl")
dump_jsonl(val, OUT_DIR/"val.jsonl")
dump_jsonl(test, OUT_DIR/"test.jsonl")
dump_jsonl(hard, OUT_DIR/"hard_test.jsonl")
dump_jsonl(data, OUT_DIR/"dataset.jsonl")

print("[Done] wrote out/ files + merged_noisy.json")