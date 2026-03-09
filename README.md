# AI-SPOC  
**AI Service Public Complaint Router**

NLP-based system for automatically classifying unstructured civil complaints and routing them to the appropriate public agency.

Developed for the **2026 Ministry of the Interior and Safety  
"AI-based Public Service Innovation Scenario and Development Method Contest" (Track 2)**.

---

# 🇺🇸 English

## Overview

In real-world public administration systems, citizens submit complaints in **free-form natural language**, not structured forms.  
This makes it difficult to determine which agency should handle each complaint.

**AI-SPOC** solves this problem using an **NLP classification pipeline** that automatically maps complaints to the most relevant public agency.

The system focuses on:

- Processing **noisy and unstructured complaint text**
- Mapping complaints to **government agencies**
- Evaluating classification performance
- Supporting **confidence-based selective routing**

---

## Key Features

- Natural language complaint classification
- Automatic mapping to public agencies
- Dataset preprocessing and validation
- Selective routing based on confidence thresholds
- Evaluation metrics and experiment analysis

---

## Repository Structure

```
ai-spoc
│
├── MinWon_Service
│   ├── batches
│   │   ├── batch01.json
│   │   ├── batch02.json
│   │   └── ...
│   │
│   ├── inject_noise_and_split.py
│   ├── merge.py
│   └── validate.py
│
├── prove
│   ├── classification_report.txt
│   ├── confusion_matrix.csv
│   ├── metrics_summary.json
│   ├── routing_distribution.json
│   └── ...
│
└── README.md
```

---

## Core Components

### MinWon_Service

Scripts for dataset preprocessing and preparation.

- **inject_noise_and_split.py**  
  Generates noisy datasets and splits them into batches.

- **merge.py**  
  Merges dataset fragments into a single dataset.

- **validate.py**  
  Performs dataset validation and integrity checks.

---

### prove

Contains experiment results and evaluation outputs such as:

- classification reports
- confusion matrices
- routing distribution
- latency analysis
- selective routing metrics

These artifacts demonstrate the performance of the routing model.

---

## Use Cases

This system can be applied to:

- Government complaint routing systems
- Public service automation
- Administrative workflow optimization
- Intelligent citizen service platforms

---

# 🇰🇷 한국어

## 프로젝트 개요

**AI-SPOC (AI Service Public Complaint Router)** 는  
비정형 자연어로 작성된 민원 데이터를 분석하여  
해당 민원을 **적절한 공공기관으로 자동 분류하는 NLP 기반 시스템**입니다.

본 프로젝트는  
**2026 행정안전부 "AI 기반 민원 서비스 혁신 시나리오 및 개발 방법 공모전" Track 2**  
제출을 위해 개발되었습니다.

실제 민원 데이터는 다음과 같은 특징을 가집니다.

- 자연어 형태의 비정형 텍스트
- 담당 기관이 명확하지 않은 경우 존재
- 여러 행정 영역이 혼합된 민원 발생

AI-SPOC는 이러한 문제를 해결하기 위해  
**Softmax 기반 다중 분류 모델**을 활용하여  
민원을 적절한 공공기관으로 자동 라우팅합니다.

---

## 주요 기능

- 자연어 민원 텍스트 자동 분류
- 공공기관 라벨 자동 매핑
- 민원 데이터 전처리 및 검증
- 신뢰도 기반 선택적 라우팅
- 모델 성능 평가 및 실험 분석

---

## 활용 가능 분야

- 공공 민원 자동 분류 시스템
- 행정 서비스 자동화
- 민원 처리 업무 효율화
- 스마트 행정 플랫폼

---

## License

This project was developed for research and contest submission purposes.
