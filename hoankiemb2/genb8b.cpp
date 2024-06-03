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

void generate_test_case(const std::string& input_filename, const std::string& output_filename, int N) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    
    int n = rand() % N + 10000;
    input_file << n << "\n";
    int kq = 0;
    while(n > 0){
        kq += n % 10;
        n /= 10;
    }
    output_file << kq << "\n";

    input_file.close();
    output_file.close();
}

signed main()
{
    srand(time(0));
    int num_tests;
    int N;
    string folder_name;

    cout << "Number of test cases:";
    cin >> num_tests;
    cout << "Max value of N: ";
    cin >> N;
    cout << "Enter file name:";
    cin>>folder_name;

    fs::create_directory(folder_name);

    for (int i = 1; i <= num_tests; ++i) {
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());

        input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        generate_test_case(input_filename.str(), output_filename.str(), N);
    }
    return 0;
}
