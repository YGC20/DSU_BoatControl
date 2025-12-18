# 🐍 Python & Conda 환경 기초

## 1️⃣ Python의 역할
Python은 인공지능 프로젝트의 핵심 언어로, 데이터 전처리, 모델 학습, 시각화까지 대부분의 과정을 담당합니다.

- **해석형 언어** → 빌드 없이 바로 실행 가능
- **광범위한 생태계** → torch, numpy, opencv, onnx 등 과학연산 및 인공지능 라이브러리 다수
- **버전 호환 중요** → PyTorch나 MMCV 같은 패키지는 Python 3.10 기준으로 최적화되어 있음

## 2️⃣ Anaconda의 역할
Anaconda는 Python 패키지 관리와 가상환경을 통합적으로 관리합니다.

- `conda create -n boatcnt python=3.10` : 새로운 가상환경 생성
- `conda activate boatcnt` : 환경 진입
- `conda list` : 패키지 목록 확인

### 왜 Conda를 쓰는가?
- 프로젝트마다 다른 버전의 패키지를 격리 가능  
- GPU/CUDA 라이브러리 버전 충돌 방지  
- 복잡한 과학 연산 패키지(numpy, scipy, torch 등) 자동 관리

## 3️⃣ pip과의 관계
- **conda** : 환경 및 기본 패키지 관리
- **pip** : 세부 라이브러리 설치  
→ 실제 프로젝트에서는 `conda`로 환경을 만들고, `pip install`로 패키지를 세부 조정

