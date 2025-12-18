
# 🧠 YOLO 기본 정리

## 📌 YOLO Model
**YOLO(You Only Look Once)** 는 객체 검출(Object Detection) 기술 중에서도 가장 대표적인 모델이다.  
이는 **On-Time Object Detection System** 으로, 딥러닝을 기반으로 한 물체 감지 및 객체 인식 접근 방식이다.

---

## 🎯 Object Detection (객체 인식)

- 이미지 또는 비디오에서 개체를 **식별하고 찾는 것**과 관련된 컴퓨터 비전 작업이다.  
- 영상처리나 Computer Vision 분야에서 널리 사용되는 핵심 기법이다.

### 주요 질문
1. **이것은 무엇인가?** (What is it?)  
2. **어디에 위치해 있는가?** (Where is it?)

---

## ⚙️ YOLO 구조 (YOLO Structure)

- 입력된 이미지를 **그리드(Grid)** 로 분할한 뒤,  
  각 그리드를 **신경망(Neural Network)** 에 통과시켜  
  **Bounding Box(Bbox)** 와 **클래스(Class)** 예측을 생성한다.
- 이후 후처리 과정을 통해 **최종 감지 출력(Final Detection Output)** 을 결정한다.

### 주요 구성 요소
- **IoU (Intersection over Union)**  
  - 모델이 예측한 Bounding Box와 실제 객체의 Bounding Box가  
    얼마나 잘 일치하는지를 평가하는 지표.
- **NMS (Non-Maximum Suppression)**  
  - 동일한 객체에 대해 여러 개의 박스가 검출될 경우,  
    **가장 높은 확률을 가진 박스만 남기고 나머지를 제거**하는 기법.

### 참고
> 객체 검출 알고리즘은 종종 특정 객체를 과도하게 감지(over-detection)하는 문제가 발생한다.  
> 즉, 실제 위치 근처에서 여러 감지 그룹이 형성되는 현상이 나타날 수 있는데,  
> 이를 해결하기 위해 NMS를 사용한다.

---

## 🔍 YOLO 동작 방식 (How YOLO Works)

1. 입력 이미지를 전체적으로 확인한다.  
2. 이미지를 **NxN 그리드**로 나눈다.  
3. 각 그리드에서 **이미지 분류(Classification)** 및 **지역화(Localization)** 작업을 수행한다.  
4. **Bbox(객체 위치 확인 및 식별)** 를 생성한다.  
5. Bounding Box와 클래스 확률을 종합해 객체를 인식하고 예측한다.

### 특징
- IoU와 NMS를 결합하여 높은 정확도의 객체 감지를 수행한다.  
- 훈련 과정에서 전체 이미지의 컨텍스트 정보를 학습해  
  **객체의 모양과 클래스 특성**을 암시적으로 인코딩한다.

---

## 🧩 핵심 요약

| 구분 | 내용 |
|------|------|
| 모델 이름 | YOLO (You Only Look Once) |
| 핵심 개념 | 객체 검출(Object Detection) |
| 주요 기술 | IoU, NMS |
| 처리 방식 | 이미지를 그리드로 분할 → 신경망 예측 → 박스 및 클래스 확률 산출 |
| 주요 특징 | 빠른 처리 속도, End-to-End 학습 가능 |

---

## 📚 참고 용어
- **Bbox (Bounding Box)** : 객체의 위치를 나타내는 사각형 좌표 정보  
- **IoU (Intersection over Union)** : 예측 박스와 실제 박스의 겹침 비율  
- **NMS (Non-Maximum Suppression)** : 중복 박스 제거 알고리즘  

---

> ✍️ 요약:  
> YOLO는 이미지를 한 번만 보고(You Only Look Once) 객체의 위치와 종류를 동시에 판단하는  
> 빠르고 효율적인 객체 검출 모델이다.
