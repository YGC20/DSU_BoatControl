#include "detector.h"
#include <onnxruntime_cxx_api.h>
#include <iostream>

class OrtDetector : public Detector {
public:
    bool load(const std::string& model_path) override {
        try {
            Ort::Env env(ORT_LOGGING_LEVEL_WARNING, "boatcnt");
            env_ = std::move(env);
            Ort::SessionOptions opt;
            // opt.SetIntraOpNumThreads(1);
            // GPU EP 붙이려면: OrtSessionOptionsAppendExecutionProvider_CUDA(opt, 0);
            session_ = std::make_unique<Ort::Session>(env_, model_path.c_str(), opt);
            allocator_ = std::make_unique<Ort::AllocatorWithDefaultOptions>();
            std::cout << "[ORT] Loaded: " << model_path << "\n";
            return true;
        } catch (const std::exception& e) {
            std::cerr << "[ORT] Load failed: " << e.what() << "\n";
            return false;
        }
    }

    std::vector<Detection> infer(const std::string& image_path) override {
        // TODO: 이미지 로드/전처리(OpenCV) → input tensor → session_.Run(...) → 후처리
        std::cout << "[ORT] Inference not implemented yet. Input: " << image_path << "\n";
        return {};
    }
private:
    Ort::Env env_{ORT_LOGGING_LEVEL_WARNING, "boatcnt"};
    std::unique_ptr<Ort::Session> session_;
    std::unique_ptr<Ort::AllocatorWithDefaultOptions> allocator_;
};

extern "C" Detector* create_detector() { return new OrtDetector(); }
