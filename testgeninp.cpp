#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <string>
#include <direct.h> // Windows specific

void generate_test_case(const std::string& input_filename, int N) {
    std::ofstream input_file(input_filename);

    // Sinh ngẫu nhiên mảng N số
    std::vector<int> array(N);
    for (int i = 0; i < N; ++i) {
        array[i] = rand() % 10000001; // Các số trong mảng <= 10^7
    }

    // Ghi vào file input
    input_file << N << "\n";
    for (int num : array) {
        input_file << num << " ";
    }
    input_file << "\n";

    input_file.close();
}

int main() {
    srand(time(0));
    int num_tests;
    int max_N;
    std::string folder_name;

    std::cout << "Nhap so luong test cases: ";
    std::cin >> num_tests;
    std::cout << "Nhap gia tri N toi da: ";
    std::cin >> max_N;
    std::cout << "Nhap ten thu muc lon: ";
    std::cin >> folder_name;

    // Tạo thư mục lớn
    _mkdir(folder_name.c_str());

    for (int i = 1; i <= num_tests; ++i) {
        int N = rand() % max_N + 1;
        std::ostringstream input_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        _mkdir(subfolder.str().c_str());

        input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";

        generate_test_case(input_filename.str(), N);
    }

    return 0;
}
