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

void generate_test_N(const std::string& input_filename, const std::string& output_filename, int A, int B, int C) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    
    int a = rand() % A;
    int b = rand() % B;
    int c = rand() % (a + b - 1) + 1;
    input_file << a << " "<< b <<" "<< c << "\n";
    string kq;
    if (a + b > c && b + c > a && c + a > b){
        kq="N";
    }
    output_file << kq << "\n";

    input_file.close();
    output_file.close();
}

void generate_test_V(const std::string& input_filename, const std::string& output_filename, int A, int B, int C) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    
    int m = rand() % A + 1; 
    int n = rand() % A + 1; 
    if (m < n) swap(m, n);

    int a = m * m - n * n;
    int b = 2 * m * n;
    int c = m * m + n * n;
    input_file << a << " "<< b <<" "<< c << "\n";
    string kq;
    if (a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a){
        kq="v";
    }
    output_file << kq << "\n";

    input_file.close();
    output_file.close();
}

void generate_test_T(const std::string& input_filename, const std::string& output_filename, int A, int B, int C) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    
    int a = rand() % A + 1; 
    int b = rand() % B + 1; 
    int c = sqrt(a * a + b * b) + rand() % 10 + 1;
    input_file << a << " "<< b <<" "<< c << "\n";
    string kq;
    if(a*a > b*b+c*c || b*b > a*a+c*c || c*c > a*a+b*b) {
        kq="T";
    }
    output_file << kq << "\n";

    input_file.close();
    output_file.close();
}

signed main()
{
    srand(time(0));
    int num_tests;
    int A, B, C;
    string folder_name;

    cout << "Number of test cases:";
    cin >> num_tests;
    cout << "Max value of A, B, C:";
    cin >> A >> B>> C;
    cout << "Enter file name:";
    cin>>folder_name;

    fs::create_directory(folder_name);

    for (int i = 1; i <= num_tests; ++i) {
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());

        input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        if(i%3==1) generate_test_N(input_filename.str(), output_filename.str(), A, B, C);
        else if(i%3==2) generate_test_T(input_filename.str(), output_filename.str(), A, B, C);
        else generate_test_V(input_filename.str(), output_filename.str(), A, B, C);
    }
    return 0;
}
