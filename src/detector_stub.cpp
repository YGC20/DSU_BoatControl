#include "detector.h"
#include <iostream>

class StubDetector : public Detector {
public:
    bool load(const std::string& model_path) override {
        std::cout << "[STUB] ONNX Runtime not enabled. Model path ignored: " << model_path << "\n";
        return true;
    }
    std::vector<Detection> infer(const std::string& image_path) override {
        std::cout << "[STUB] Pretending to run inference on: " << image_path << "\n";
        // 빈 결과 반환 (파이프라인만 확인)
        return {};
    }
};

extern "C" Detector* create_detector() { return new StubDetector(); }
