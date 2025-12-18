# 🔥 PyTorch 기본 구조와 CUDA 사용

## 1️⃣ PyTorch란?
딥러닝 프레임워크로, **텐서(Tensor)** 연산과 **자동 미분(Autograd)** 기능을 제공합니다.

- 유연하고 직관적인 동적 그래프 구조
- GPU 가속(CUDA) 지원
- 다양한 모델 학습 프레임워크(MMDetection, YOLO 등)의 기반

## 2️⃣ 주요 개념
### Tensor
Numpy 배열과 유사하지만 GPU 연산이 가능.

```python
import torch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print(x.device)  # cuda 또는 cpu
```

### Autograd
연산 그래프를 자동으로 만들어 미분 계산을 수행.
```python
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2
y.backward()
print(x.grad)  # dy/dx = 6
```

### CUDA 사용 여부 확인
```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

## 3️⃣ 프로젝트에서의 역할
- **모델 학습 엔진** : RT-DETR, YOLO 등 모든 신경망의 기반
- **모델 내보내기** : ONNX 변환 시 내부 연산 그래프 제공
- **CUDA 연산 관리** : GPU 메모리, 연산 최적화 담당

