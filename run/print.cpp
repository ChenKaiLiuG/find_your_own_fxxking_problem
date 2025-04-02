// Under debugging because of general physic
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    fs::path current_path = fs::
    fs::path file_path = current_path / "找找自己問題.txt";

    std::ifstream file(file_path);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    } else {
        std::cerr << "無法開啟檔案: " << file_path << std::endl;
    }

    return 0;
}
