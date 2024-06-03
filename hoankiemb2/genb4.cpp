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
    
    int M = rand() % N;
    if(M == 0) M+=2;
    else if(M == 1) M++;
    if(M == 9) M--;
    input_file << M << "\n";
    string kq;
    if(M == 2){
        kq="Monday";
    }
    else if(M == 3){
        kq="Tuesday";
    }
    else if(M == 4){
        kq="Wednesday";
    }
    else if(M == 5){
        kq="Thursday";
    }
    else if(M == 6){
        kq="Friday";
    }
    else if(M == 7){
        kq="Saturday";
    }
    else if(M == 8){
        kq="Sunday";
    }
    else if(M == 9){
        M--;
        kq="Sunday";
    }
    output_file << kq << "\n";

    input_file.close();
    output_file.close();
}

signed main()
{
    srand(time(0));
    int num_tests;
    int max_N;
    string folder_name;

    cout << "Number of test cases:";
    cin >> num_tests;
    cout << "Max value of N:";
    cin >> max_N;
    cout << "Enter file name:";
    cin>>folder_name;

    fs::create_directory(folder_name);

    for (int i = 1; i <= num_tests; ++i) {
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());

        input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        generate_test_case(input_filename.str(), output_filename.str(), max_N);
    }
    return 0;
}
