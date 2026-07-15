cmake_minimum_required(VERSION 3.20)
project(boatcnt_infer CXX)
set(CMAKE_CXX_STANDARD 17)

# ---- 옵션: 나중에 ORT 준비되면 -DUSE_ORT=ON 으로 켜기 ----
option(USE_ORT "Enable ONNX Runtime backend" OFF)

# ---- 공통 컴파일 타깃 ----
add_executable(boatcnt
    src/main.cpp
    src/detector.h
    src/detector_stub.cpp
)

# ---- ORT 사용 시 전환 ----
if(USE_ORT)
    message(STATUS "Building with ONNX Runtime backend")

    # ONNXRUNTIME_ROOT를 CMake 옵션으로 넘기거나, 여기서 직접 셋업
    if(NOT DEFINED ONNXRUNTIME_ROOT)
        message(FATAL_ERROR "Please set -DONNXRUNTIME_ROOT=path/to/onnxruntime")
    endif()

    # 헤더/라이브러리 등록
    target_include_directories(boatcnt PRIVATE "${ONNXRUNTIME_ROOT}/include")
    add_library(onnxruntime SHARED IMPORTED)
    set_target_properties(onnxruntime PROPERTIES
        IMPORTED_IMPLIB "${ONNXRUNTIME_ROOT}/lib/onnxruntime.lib"
        IMPORTED_LOCATION "${ONNXRUNTIME_ROOT}/bin/onnxruntime.dll"
    )
    target_link_libraries(boatcnt PRIVATE onnxruntime)

    # ORT 구현파일로 스텁 대체
    target_sources(boatcnt PRIVATE src/detector_onnxruntime.cpp)
    # 스텁은 제외하고 싶다면:
    # set_source_files_properties(src/detector_stub.cpp PROPERTIES HEADER_FILE_ONLY ON)
endif()

# ---- (선택) OpenCV 나중에 연결하고 싶다면 여기 find_package(OpenCV REQUIRED) 추가 ----
# find_package(OpenCV REQUIRED)
# target_link_libraries(boatcnt PRIVATE ${OpenCV_LIBS})
