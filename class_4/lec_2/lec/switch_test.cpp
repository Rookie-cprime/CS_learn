#include <iostream>
using namespace std;

int main()
{
    double arg1,arg2,result;
    char temp;
    cout<<"Please input a math expression"<<endl;
    cin>>arg1>>temp>>arg2;
    switch(temp){
        case '*':
            result = arg1*arg2;
            cout<<result<<endl;
            break;
        case '+':
            result = arg1+arg2;
            cout<<result<<endl;
            break;
        case '-':
            result = arg1-arg2;
            cout<<result<<endl;
            break;
        case '/':
            result = arg1/arg2;
            cout<<result<<endl;
            break;
        default:
            cout<<"You input is illegal"<<endl;
    }
    return 0;
}

