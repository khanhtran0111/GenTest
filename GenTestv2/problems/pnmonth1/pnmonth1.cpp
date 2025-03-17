#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int a; cin >> a;
    if(a == 1 || a == 3 || a == 5 || a == 7 || a == 8 || a == 10 || a == 12) cout << "31";
    else if(a == 2) cout << "28";
    else cout << "30";
    return 0;
}