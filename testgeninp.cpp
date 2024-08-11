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

void generate_test_case(const std::string& input_filename, const std::string& output_filename, int M) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    //Your code to generate test case here
    // M is the limit for your testcase. You can easily set it up
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
    cout << "Max value of N:";
    cin >> max_N;
    cout << "Enter file name:";
    cin>>folder_name;
    
    fs::create_directory(folder_name);

    for (int i = 1; i <= num_tests; i++) {
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());
        //if you only gen input file and want to name it with test00x.inp and test00x.out (with x is the number of test case), you can use this code
        // input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        // output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        //this code will help you to sun your solution code to have correct output.
        input_filename << subfolder.str() << "/" << folder_name << ".inp";
        output_filename << subfolder.str() << "/" << folder_name << ".out";

        generate_test_case(input_filename.str(), output_filename.str(), max_N);
    }

    return 0;
}
