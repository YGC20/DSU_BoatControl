#include "detector.h"
#include <iostream>
#include <memory>

extern "C" Detector* create_detector(); // 각각 cpp에서 구현

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cout << "Usage:\n  boatcnt <model.onnx> <image_path>\n";
        std::cout << "Tip: Without ONNX Runtime, this runs in STUB mode.\n";
        return 0;
    }
    std::string model = argv[1];
    std::string img   = argv[2];

    std::unique_ptr<Detector> det(create_detector());
    if (!det->load(model)) {
        std::cerr << "Failed to load model\n";
        return 1;
    }
    auto results = det->infer(img);
    std::cout << "Detections: " << results.size() << "\n";
    return 0;
}
