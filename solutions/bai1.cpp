#include<bits/stdc++.h>
using namespace std;

signed main(){
    int n;
    cin>>n;
    int a[n+5];
    int s = 0;
    for(int i=1; i <= n; i++){
        cin>>a[i];
        s += a[i];
    }
    cout<<s;
    return 0;
}