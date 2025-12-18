
# ⚙️ YOLO 발생 문제 및 해결 정리

## 🧩 문제 개요

라즈베리파이에서 YOLO 모델의 **`detect.py`** 결과를  
다른 코드에서 활용하기 위한 기능을 추가하던 중 오류 발생.

---

## 🔧 코드 수정 내역

### ✅ 수정된 파일: `detect.py`

```python
# Run inference
model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup

seen, windows, dt = 0, [], (Profile(device=device), Profile(device=device), Profile(device=device))
detected_objects = []  # 리스트를 초기화하여 감지된 물체의 정보를 저장

for path, im, im0s, vid_cap, s in dataset:
    with dt[0]:
        # ... (기존 코드 생략)

    # Process predictions
    for i, det in enumerate(pred):  # per image
        seen += 1

        if webcam:
            p, im0, frame = path[i], im0s[i].copy(), dataset.count
            s += f"{i}: "

            for *xyxy, conf, cls in reversed(det):
                c = int(cls)
                label = names[c] if hide_conf else f"{names[c]}"
                confidence = float(conf)
                confidence_str = f"{confidence:.2f}"

                detected_objects.append({
                    "label": label,
                    "confidence": confidence_str,
                    "coordinates": xyxy
                })
        else:
            p, im0, frame = path, im0s.copy(), getattr(dataset, "frame", 0)

            for *xyxy, conf, cls in reversed(det):
                c = int(cls)
                label = names[c] if hide_conf else f"{names[c]}"
                confidence = float(conf)
                confidence_str = f"{confidence:.2f}"

                detected_objects.append({
                    "label": label,
                    "confidence": confidence_str,
                    "coordinates": xyxy
                })

# ... (기존 코드 생략)
return detected_objects
```

---

### 🆕 새로 추가된 파일: `check_object.py`

```python
from detect_module import detect_objects

# detect_objects 함수 호출
detected_objects_info = detect_objects(weights='yolov5s.pt', source='0')

# 반환된 정보 출력
for obj_info in detected_objects_info:
    print(obj_info)
```

---

## ⚠️ 발생한 오류

라즈베리파이에서 `check_object.py` 실행 시 다음 오류 발생:

```
Profile.__init__() got an unexpected keyword argument 'device'
terminate called without an active exception
Aborted
```

### 🔍 오류 원인 분석
- `Profile` 클래스 초기화 시 `device`라는 인자를 인식하지 못함.  
- 즉, **`device` 인자가 허용되지 않는데 전달되어 예외 발생.**

---

## 💡 개념 정리

### 🔸 device란?

PyTorch에서 모델을 실행할 **디바이스(CPU 또는 GPU)** 를 지정하는 매개변수.

| 예시 | 설명 |
|------|------|
| `cuda:0` | 첫 번째 GPU 사용 |
| `cuda:1`, `cuda:2` | 두 번째, 세 번째 GPU 사용 |
| `cpu` | CPU 사용 (CUDA 미지원 환경에서 기본) |

> GPU는 병렬 연산이 가능해 속도가 빠르지만,  
> 라즈베리파이는 일반적으로 CUDA를 지원하지 않는다.

---

## 🧠 문제 해결 과정

라즈베리파이는 ARM 아키텍처 기반으로 CUDA를 사용할 수 없기 때문에,  
**`device='cpu'`** 로 지정하여 모델을 CPU에서 실행하도록 수정함.

---

## ✅ 수정된 코드 (`check_object.py`)

```python
from detect import run

detected_objects_info = run(weights='yolov5s.pt', source='0', device='cpu')

for obj_info in detected_objects_info:
    print(obj_info)
```

---

## 🎯 해결 결과

- `Profile` 초기화 오류 해결 ✅  
- 라즈베리파이 환경에서도 YOLO 모델 정상 작동 ✅  
- 감지된 객체 정보를 외부 코드에서 받아 활용 가능 ✅

---

## 📘 요약

| 항목 | 내용 |
|------|------|
| 문제 | `Profile.__init__()`에 `device` 인자 전달 오류 |
| 원인 | `Profile` 클래스가 `device` 인자를 지원하지 않음 |
| 환경 | 라즈베리파이 (CUDA 미지원) |
| 해결 방법 | `device='cpu'` 지정 |
| 결과 | 모델 정상 작동 및 객체 정보 전달 성공 |

---

> 📝 **정리:**  
> 라즈베리파이처럼 CUDA가 없는 환경에서는 PyTorch 모델을 CPU에서 실행하도록 명시해야 한다.  
> 이를 통해 불필요한 디바이스 관련 오류를 방지할 수 있다.
