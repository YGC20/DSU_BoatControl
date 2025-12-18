# 🚀 RT-DETR 모델 구조

## 1️⃣ DETR의 기본 아이디어
DETR은 CNN + Transformer를 결합하여 **객체 탐지(object detection)** 를 end-to-end 방식으로 수행합니다.

### 구조 요약
- **Backbone** : 이미지 특징 추출 (ResNet, CSPNet 등)
- **Encoder** : 전역 문맥(feature) 관계 학습
- **Decoder** : 객체 후보와 실제 물체 매칭 (Hungarian Matching)
- **Prediction Head** : 바운딩 박스 + 클래스 확률 출력

## 2️⃣ RT-DETR의 차별점 (Real-Time DETR)
- 기존 DETR은 느림 → **RT-DETR은 Anchor-free, Efficient Attention** 사용  
- **CNN-Transformer 혼합 백본**으로 속도 개선  
- ONNX/TensorRT 최적화 시 실시간 성능 확보

## 3️⃣ 출력 구조
| 이름 | 설명 |
|------|------|
| `bboxes` | [x1, y1, x2, y2] 형태의 탐지 결과 |
| `scores` | 각 클래스의 확률 |
| `labels` | 클래스 인덱스 |

## 4️⃣ 프로젝트에서의 역할
- 차량/객체 탐지의 핵심 백본  
- YOLO 대비 고정밀, 라이선스 제약 적음  
- ONNX 내보내기와 TensorRT 가속 모두 안정적으로 지원

