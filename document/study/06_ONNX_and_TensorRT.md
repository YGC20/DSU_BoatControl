# ⚙️ ONNX & TensorRT 배포

### 1️⃣ ONNX란?
Open Neural Network Exchange — 다양한 프레임워크 간 모델 호환 표준 포맷.

#### ONNX Runtime
ONNX Runtime은 ONNX 형식으로 저장된 모델을 효율적으로 실행하기 위한 고성능 추론 엔진입니다. 이 라이브러리 자체는 AI 모델을 포함하지 않으며, 사용자가 준비한 `.onnx` 모델 파일을 로드하여 추론을 수행하는 역할을 합니다.

### 내보내기
```bash
python tools/deployment/pytorch2onnx.py
```

### 단순화
```bash
python -m onnxsim models/rtdetr_l.onnx models/rtdetr_l.sim.onnx
```

## 2️⃣ TensorRT
- NVIDIA의 고성능 추론 엔진
- FP16, INT8 정밀도 최적화 가능

### 변환
```bash
trtexec --onnx=models/rtdetr_l.sim.onnx --saveEngine=models/rtdetr.engine --fp16
```

## 3️⃣ 장점
| 항목 | ONNX | TensorRT |
|------|------|-----------|
| 속도 | 중간 | 최고 |
| 호환성 | 매우 높음 | GPU 한정 |
| 사용 편의성 | Python/C++ 모두 지원 | 주로 C++ |

