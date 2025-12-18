# ⚙️ ONNX & TensorRT 배포

## 1️⃣ ONNX란?
Open Neural Network Exchange — 다양한 프레임워크 간 모델 호환 표준 포맷.

### 내보내기
```bash
python tools/deployment/pytorch2onnx.py   configs/rtdetr/rtdetr-l_8xb16-36e_coco.py   work_dirs/rtdetr_l_mydata/epoch_36.pth   --output-file models/rtdetr_l.onnx   --shape 640 640 --opset 12 --dynamic-export
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

