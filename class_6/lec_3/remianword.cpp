#include <iostream>
#include <string>
using namespace std;

string remainingwords(string s);


int main()
{
    cout << remainingwords("the quick brown fox");
    return 0;
}

string remainingwords(string s){
    string remain;
    int pos;
    pos = s.find(" ");
    if(pos != s.npos)
        return s.substr(pos+1);
    else 
        return "";
}

