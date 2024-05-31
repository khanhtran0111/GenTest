#include<bits/stdc++.h>
//#define int long long
#define speed ios_base::sync_with_stdio(0); cin.tie(0);

#define fi first
#define se second
#define taskname ""
using namespace std;
const int maxn=1e5+10;
const int mod=1e9+7;

namespace fs = std::filesystem;

string generate_random_string(size_t n){
    auto randchar =[]() -> char {
        const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        const size_t max_index = (sizeof(charset) - 1);
        return charset[rand() % max_index];
    };
    string str(n, 0);
    generate_n(str.begin(), n, randchar);
    return str;
}

void generate_test_case(const std::string& input_filename, const std::string& output_filename, int N) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);

    string ss = generate_random_string(N);
    input_file << ss;
    output_file<< ss;
    input_file.close();
    output_file.close();
}

int main() {
    srand(time(0));
    int num_tests;
    int max_N;
    string folder_name;

    cout << "Number of test cases:";
    cin >> num_tests;
    cout << "Max length of string:";
    cin >> max_N;
    cout << "Enter file name:";
    getline(cin, folder_name);

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