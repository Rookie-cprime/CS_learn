#include <iostream>
#include <string>
using namespace std;

int main()
{
    int i;
    string userName;
    string outName;
    cout<<"Please enter your name:"<<endl;
    getline(cin,userName);
    for (i = userName.length()-1;i >= 0;i--){
        cout<<userName[i];
    }
    cout<<endl;
    return 0;
}

