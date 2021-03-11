#include <iostream>
#include <string>
using namespace std;

int main()
{
    char a;
    int b;
    cout<<"Enter a character:";
    cin>>a;
    b = a;
    if(b>=48&&b<=57)
        cout<<a<<" is a digit."<<endl;
    else if(b>=65&&b<=90)
        cout<<a<<" is a upper case letter."<<endl;
    else if(b>=97 && b<=122)
        cout<<a<<" is a lower case letter."<<endl;
    else
        cout<<a<<" is a non-alphanumeric  character."<<endl;
}

