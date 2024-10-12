#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include<vector>
#define int long long
#define speed ios_base::sync_with_stdio(0); cin.tie(0);

#define fi first
#define se second
#define taskname ""
using namespace std;
const int maxn=1e5+10;
const int mod=1e9+7;

namespace fs = std::filesystem;

int randomInRange(int a, int b){
    return a + rand() % (b-a+1);
}


void generate_test_case(const std::string& input_filename, const std::string& output_filename, int M) {
    ofstream input_file(input_filename);
    ofstream output_file(output_filename);
    // M is the limit for your testcase. You can easily set it up
    int N = (rand() % M + M)%M; //just example, you have to create your know number that suit with your problem.
    //double N = (static_cast<double>(rand()) / RAND_MAX) * (3 * M + 1) - M; both negative and positive numbers
    //double N = (static_cast<double>(rand()) / RAND_MAX) * M; only positive numbers
    //int Even = 2 * (rand() % (M / 2));
    //int Odd = 2 * (rand() % (M / 2)) + 1;
    input_file << N << "\n";
    //output_file << N << "\n";

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

    for (int i = 1; i <= num_tests; i++) {
        std::ostringstream input_filename, output_filename, subfolder;

        subfolder << folder_name << "/test" << std::setw(3) << std::setfill('0') << i;
        fs::create_directory(subfolder.str());

        // input_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".inp";
        // output_filename << subfolder.str() << "/test" << std::setw(3) << std::setfill('0') << i << ".out";

        input_filename << subfolder.str() << "/" << folder_name << ".inp";
        output_filename << subfolder.str() << "/" << folder_name << ".out";


        generate_test_case(input_filename.str(), output_filename.str(), max_N);
    }
    return 0;
}
