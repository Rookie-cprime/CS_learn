#include <iostream>
using namespace std;

int main()
{
    int lowletter_up,lowletter_down,upletter_up,upletter_down,judge_num;
    lowletter_down = 'a';
    lowletter_up  = 'a'+26;
    upletter_down = 'A';
    upletter_up = 'A'+26;
    char  inputletter;
    cout<<"Please input a charactor"<<endl;
    cin>>inputletter;
    judge_num=inputletter;
    if(judge_num<=lowletter_up && judge_num>=lowletter_down)
        cout<<"It's lowercase"<<endl;
    else
        cout<<"It's uppercase"<<endl;
    
    return 0;
}

