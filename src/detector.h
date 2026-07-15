#pragma once
#include <string>
#include <vector>
#include <utility>

struct Detection {
    int    class_id{};
    float  score{};
    // x1,y1,x2,y2
    float  x1{}, y1{}, x2{}, y2{};
};

class Detector {
public:
    virtual ~Detector() = default;
    virtual bool load(const std::string& model_path) = 0;
    virtual std::vector<Detection> infer(const std::string& image_path) = 0;
};
