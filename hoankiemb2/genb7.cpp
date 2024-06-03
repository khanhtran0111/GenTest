#include<bits/stdc++.h>
#define int long long
#define speed ios_base::sync_with_stdio(0); cin.tie(0);

#define fi first
#define se second
#define taskname ""
using namespace std;
const int maxn=1e5+10;
const int mod=1e9+7;

namespace fs = std::filesystem;

void generate_test_case1(const std::string& input_filename, const std::string& output_filename, int N, int C) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    int M, x;
    int c = rand() % C + 1;
    if(c > 12) c--;
    x = rand() % N + 1;
    if(x % 4 == 0) M = x;
    else if(x % 4 != 0) M = x - (x%4);
    input_file << M <<" "<< c << "\n";
    string kq;
    if(M % 400 == 0 || (M % 4 == 0 && M % 100 != 0)){
        if(c == 2) kq="29";
        else if(c == 1 || c == 3 || c == 5 || c == 7 || c == 8 || c == 10 || c == 12) kq="31";
        else kq="30";
    }
    else{
        if(c == 2) kq="28";
        else if(c == 1 || c == 3 || c == 5 || c == 7 || c == 8 || c == 10 || c == 12) kq="31";
        else kq="30";
    }
    output_file << kq << "\n";
    input_file.close();
    output_file.close();
}

void generate_test_case2(const std::string& input_filename, const std::string& output_filename, int N, int C) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    int M, x;
    x = rand() % N + 1;
    if(x % 100 == 0) M = x;
    else if(x % 100 != 0) M = x - (x%100);
    int c = rand() % C + 1;
    if(c > 12) c--;
    input_file << M <<" "<< c << "\n";
    string kq;
    if(M % 400 == 0 || (M % 4 == 0 && M % 100 != 0)){
        if(c == 2) kq="29";
        else if(c == 1 || c == 3 || c == 5 || c == 7 || c == 8 || c == 10 || c == 12) kq="31";
        else kq="30";
    }
    else{
        if(c == 2) kq="28";
        else if(c == 1 || c == 3 || c == 5 || c == 7 || c == 8 || c == 10 || c == 12) kq="31";
        else kq="30";
    }
    output_file << kq << "\n";
    input_file.close();
    output_file.close();
}

void generate_test_case3(const std::string& input_filename, const std::string& output_filename, int N, int C) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    int M, x;
    M = rand() % N + 1;
    int c = rand() % C + 1;
    if(c > 12) c--;
    input_file << M <<" "<< c << "\n";
    string kq;
    if(M % 400 == 0 || (M % 4 == 0 && M % 100 != 0)){
        if(c == 2) kq="29";
        else if(c == 1 || c == 3 || c == 5 || c == 7 || c == 8 || c == 10 || c == 12) kq="31";
        else kq="30";
    }
    else{
        if(c == 2) kq="28";
        else if(c == 1 || c == 3 || c == 5 || c == 7 || c == 8 || c == 10 || c == 12) kq="31";
        else kq="30";
    }
    output_file << kq << "\n";
    input_file.close();
    output_file.close();
}

signed main()
{
    srand(time(0));
    int num_tests;
    int max_N, max_month;
    string folder_name;

    cout << "Number of test cases:";
    cin >> num_tests;
    cout << "Max value of N and Month:";
    cin >> max_N >> max_month;
    cout << "Enter file name:";
    cin>>folder_name;

    fs::create_directory(folder_name);

    for (int i = 1; i <= num_tests; ++i) {
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());

        input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        if(i % 3 == 1) generate_test_case1(input_filename.str(), output_filename.str(), max_N, max_month);
        else if(i % 3 == 2) generate_test_case2(input_filename.str(), output_filename.str(), max_N, max_month);
        else generate_test_case3(input_filename.str(), output_filename.str(), max_N,max_month);
    }
    return 0;
}
