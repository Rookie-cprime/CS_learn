#include <iostream>
#include <string>
using namespace std;

string firstword (string s);

int main()
{
    cout << firstword("the quick brown fox")<<endl;
    return 0;
}

string firstword (string s){
    string first_word;
    int pos;
    pos = s.find(" ");
    if(pos != s.npos)
        return s.substr(0,pos);
    else
        return s;
}




