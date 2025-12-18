# 🖥️ C++ 추론 환경 구성 (ONNX Runtime 기반)

## 1️⃣ 필요한 도구
- **Visual Studio 2022** (C++ 데스크톱 개발)
- **CMake 3.27+**
- **vcpkg** (패키지 매니저)

## 2️⃣ vcpkg 설치
```bash
git clone https://github.com/microsoft/vcpkg
.cpkgootstrap-vcpkg.bat
.cpkg install onnxruntime opencv fmt spdlog
```

## 3️⃣ CMakeLists.txt 예시
```cmake
cmake_minimum_required(VERSION 3.20)
project(rtdetr_infer CXX)
set(CMAKE_CXX_STANDARD 17)

find_package(OpenCV REQUIRED)
find_package(onnxruntime REQUIRED)
find_package(fmt REQUIRED)
find_package(spdlog REQUIRED)

add_executable(rtdetr src/main.cpp)
target_link_libraries(rtdetr PRIVATE ${OpenCV_LIBS} onnxruntime::onnxruntime fmt::fmt spdlog::spdlog)
```

## 4️⃣ main.cpp 예시 (요약)
```cpp
#include <opencv2/opencv.hpp>
#include <onnxruntime_cxx_api.h>

int main() {
    cv::Mat img = cv::imread("demo.jpg");
    // 전처리 → onnxruntime 추론 → 후처리
}
```

## 5️⃣ 빌드
```bash
cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE="path\to\vcpkg\scripts\buildsystems\vcpkg.cmake"
cmake --build build --config Release
```

## 6️⃣ 결과
ONNX Runtime을 이용해 Python 없이도 고속 추론이 가능합니다.
