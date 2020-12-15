#include <iostream>
using namespace std;

int main()
{
    int n1,n2,temp,cnt;
    n1 = 0;
    n2 = 1;
    cout<<"Please enter a positive integer greater than 1:4:";
    cin>>cnt;
    while(cnt-1 >= 0){
        cout<<n2<<endl;
        temp = n2;
        n2 = n2+n1;
        n1 = temp;
        cnt--   ;
    }
    return 0;
}

