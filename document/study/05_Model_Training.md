# 🧠 모델 학습 및 Config 수정

## 1️⃣ 데이터셋 준비 (COCO 포맷)
```
datasets/mycoco/
 ├─ annotations/
 │   ├─ instances_train.json
 │   └─ instances_val.json
 ├─ train/
 └─ val/
```
`instances_*.json`에는 이미지 파일명, 바운딩 박스, 클래스 정보 포함.

## 2️⃣ Config 수정
```bash
configs/rtdetr/rtdetr-l_8xb16-36e_coco.py
```
수정 포인트:
```python
model.bbox_head.num_classes = 3  # 예: 차량, 사람, 신호등
train_dataloader.batch_size = 8
train_dataloader.dataset.ann_file = 'datasets/mycoco/annotations/instances_train.json'
train_dataloader.dataset.data_prefix.img = 'datasets/mycoco/train/'
```

## 3️⃣ 학습 명령어
```bash
python tools/train.py configs/rtdetr/rtdetr-l_8xb16-36e_coco.py     --work-dir work_dirs/rtdetr_l_mydata
```

## 4️⃣ 평가 명령어
```bash
python tools/test.py configs/rtdetr/rtdetr-l_8xb16-36e_coco.py     work_dirs/rtdetr_l_mydata/epoch_36.pth
```

## 5️⃣ 학습 결과
- **work_dirs/** 아래 로그, 가중치 저장
- TensorBoard나 W&B 연동으로 시각화 가능

