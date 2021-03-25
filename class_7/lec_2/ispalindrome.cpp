#include <iostream>
#include <string>
using namespace std;

bool is_palindrome(string str){
    if(str.size() == 1||str == "")
        return true;
    else if(str[0] != str[str.size()-1])
        return false;
    else
        return is_palindrome(str.substr(1,str.size()-2));
}


int main()
{
    string str;
    cout<<"Please input the string:"<<endl;
    cin>>str;
    if(is_palindrome(str))
        cout<<str<<" is palindrome"<<endl;
    else
        cout<<str<<" is not palindrome"<<endl;
    
    return 0;
}

