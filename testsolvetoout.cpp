#include <bits/stdc++.h>
#define speed ios_base::sync_with_stdio(0); cin.tie(0);

using namespace std;

signed main(int argc, char* argv[])
{
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " <input file base name>" << endl;
        return 1;
    }
    
    string base_name = argv[1];

    if (ifstream(base_name + ".inp")) {
        freopen((base_name + ".inp").c_str(), "r", stdin);
        freopen((base_name + ".out").c_str(), "w", stdout);
    } else {
        cerr << "File " << base_name << ".inp not found." << endl;
        return 1;
    }
    
    speed
    
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    
    int sum = 0;
    for (int i = 1; i <= n; i++) sum += a[i];
    
    cout << sum;
    return 0;
}
