#include <iostream>
using namespace std;

int main()
{
    int n,i,j;
    int cnt;
    cnt = 1;
    cout<<"Please enter a positive integer:";
    cin>>n;
    while(cnt != n+1){
        cout<<2*cnt++<<endl;
    }
    return 0;
}

