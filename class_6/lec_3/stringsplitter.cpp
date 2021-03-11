#include <iostream>
#include <string>
using namespace std;

int main()
{
    int half;
    string strs;
    cout<<"Enter an odd length string:";
    getline(cin,strs);
    half = strs.length()/2;
    cout<<"Middle character:"+strs.substr(half,1)<<endl;
    cout<<"First half:"+strs.substr(0,half)<<endl;
    cout<<"Second half:"+strs.substr(half+1)<<endl;
}

