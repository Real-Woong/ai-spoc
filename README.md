# AI-SPOC
AI-based Public Complaint Routing System

---

# 🇺🇸 English

## Overview

**AI-SPOC (AI Service Public Complaint Router)** is an NLP-based system designed to automatically classify unstructured civil complaints into the most appropriate public agency.

The project was developed for the **2026 Ministry of the Interior and Safety AI Public Service Innovation Contest (Track 2)**.

In real public administration environments, civil complaints are typically submitted in free-form natural language rather than structured formats. This makes it difficult to determine which organization or department should handle each request.

AI-SPOC addresses this challenge by using a **softmax-based NLP classification pipeline** to route complaints to the correct government agency.

---

## Key Features

- Classification of natural language civil complaints
- Automatic mapping of complaints to public agencies
- Dataset validation and preprocessing pipeline
- Selective routing strategy based on confidence scores
- Evaluation metrics and experiment analysis

---

## Project Structure

ai-spoc
│
├── MinWon_Service
│   ├── batches
│   │   ├── batch01.json
│   │   └── …
│   ├── inject_noise_and_split.py
│   ├── merge.py
│   └── validate.py
│
├── prove
│   ├── classification_report.txt
│   ├── confusion_matrix.csv
│   ├── metrics_summary.json
│   ├── routing_distribution.json
│   └── …
│
└── README.md

---

## Core Components

### MinWon_Service

Contains scripts for dataset preparation and preprocessing.

- **inject_noise_and_split.py**  
  Generates noisy datasets and splits them into batches.

- **merge.py**  
  Merges dataset fragments into a unified dataset.

- **validate.py**  
  Performs dataset validation and integrity checks.

---

### prove

Stores experiment results and evaluation outputs.

Examples include:

- classification reports
- confusion matrices
- model configuration
- routing distribution
- selective routing performance metrics

---

## Experiment Outputs

The repository includes evaluation artifacts such as:

- Classification reports
- Confusion matrices
- Latency analysis
- Prediction distribution
- Selective routing curves

These results demonstrate the effectiveness of the routing approach.

---

## Use Case

This system can be applied to:

- Government complaint routing systems
- Public service automation
- Administrative workflow optimization
- Intelligent citizen service platforms

---

## License

This project was developed for research and contest submission purposes.


⸻

🇰🇷 한국어

프로젝트 개요

AI-SPOC (AI Service Public Complaint Router) 는
비정형 자연어로 작성된 민원 데이터를 분석하여
해당 민원을 적절한 공공기관으로 자동 분류하는 NLP 기반 시스템입니다.

본 프로젝트는
2026 행정안전부 “AI 기반 민원 서비스 혁신 시나리오 및 개발 방법 공모전” Track 2
제출을 위해 개발되었습니다.

실제 민원 데이터는 다음과 같은 특징을 가집니다.
	•	자연어 형태로 작성된 비정형 텍스트
	•	담당 기관이 명확하지 않은 경우 존재
	•	여러 행정 영역이 혼합된 민원 발생

AI-SPOC는 이러한 문제를 해결하기 위해
Softmax 기반 다중 분류 NLP 모델을 활용하여
민원을 적절한 공공기관으로 자동 라우팅합니다.

⸻

주요 기능
	•	자연어 민원 텍스트 자동 분류
	•	공공기관 라벨 자동 매핑
	•	민원 데이터 전처리 및 검증
	•	신뢰도 기반 선택적 라우팅 (Selective Routing)
	•	모델 성능 평가 및 실험 분석

⸻

프로젝트 구조

ai-spoc
│
├── MinWon_Service
│   ├── batches
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


⸻

주요 구성 요소

MinWon_Service

데이터셋 생성 및 전처리 관련 스크립트가 포함되어 있습니다.
	•	inject_noise_and_split.py
노이즈를 추가한 데이터셋을 생성하고 배치로 분할
	•	merge.py
데이터셋을 하나의 통합 데이터로 병합
	•	validate.py
데이터셋 무결성 검증

⸻

prove

모델 실험 결과 및 평가 지표가 저장된 디렉토리입니다.

포함된 내용 예시:
	•	classification report
	•	confusion matrix
	•	routing distribution
	•	selective routing 성능 분석
	•	모델 설정 정보

⸻

활용 가능 분야
	•	공공 민원 자동 분류 시스템
	•	행정 서비스 자동화
	•	민원 처리 업무 효율화
	•	스마트 행정 플랫폼

⸻

License

본 프로젝트는 연구 및 공모전 제출 목적으로 개발되었습니다.
