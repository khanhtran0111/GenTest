#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main(){
    long long n; cin>>n;
    long long x=ceil((double)(sqrt(n)));
    if(x*x==n)
    {
        x=x+2;
        cout<<(long long)x*x;
    }
    else{
        x++;
        cout<<(long long)x*x;
    }
}