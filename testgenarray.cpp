#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <filesystem> // Thêm thư viện này

namespace fs = std::filesystem;

void generate_test_case(const std::string& input_filename, const std::string& output_filename, int N) {
    std::ofstream input_file(input_filename);
    std::ofstream output_file(output_filename);

    // Sinh ngẫu nhiên mảng N số
    std::vector<int> array(N);
    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        array[i] = rand() % 10000001; // Các số trong mảng <= 10^7
        sum += array[i];
    }

    // Ghi vào file input
    input_file << N << "\n";
    for (int num : array) {
        input_file << num << " ";
    }
    input_file << "\n";

    // Ghi vào file output (ví dụ: tổng của mảng)
    output_file << sum << "\n";

    input_file.close();
    output_file.close();
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
    fs::create_directory(folder_name);

    for (int i = 1; i <= num_tests; ++i) {
        int N = rand() % max_N + 1;
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());

        input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        generate_test_case(input_filename.str(), output_filename.str(), N);
    }

    return 0;
}
