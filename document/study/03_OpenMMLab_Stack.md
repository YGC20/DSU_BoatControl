# 🧩 OpenMMLab 스택 구조

## 1️⃣ 구성요소
| 라이브러리 | 역할 |
|------------|------|
| **MMEngine** | 학습 루프, 로거, Config 관리 등 기본 엔진 |
| **MMCV** | 이미지 처리, Conv 연산, NMS 등 커스텀 연산 |
| **MMDetection** | 객체 탐지 프레임워크 (YOLO, RT-DETR 포함) |

## 2️⃣ 동작 흐름
1. **MMEngine**이 전체 학습 파이프라인 관리  
2. **MMCV**가 모델 내부 연산(NMS, DeformConv 등)을 가속  
3. **MMDetection**은 모델 구조와 데이터 로더를 정의

## 3️⃣ Config 시스템
모델 설정은 `.py` 형식으로 되어 있으며, 하이퍼파라미터를 손쉽게 조정 가능.
```bash
configs/rtdetr/rtdetr-l_8xb16-36e_coco.py
```
- `model.bbox_head.num_classes` : 클래스 수
- `train_dataloader.batch_size` : 배치 크기

## 4️⃣ 장점
- 일관된 구조로 다양한 모델 간 교체가 쉬움  
- 모듈화되어 연구/산업용 모두 적합  
- Apache-2.0 라이선스로 방위산업 프로젝트에도 안전하게 사용 가능

