#include <iostream>
using namespace std;

int main()
{
    int userInput,absvalue;
    cout<<"Please enter an integer:"<<endl;
    cin>>userInput;
    absvalue = userInput;
    if(userInput<0)
        absvalue  =userInput*(-1);
    cout<<"The absolute of "<<userInput<<" is "<<absvalue<<endl;
    return 0;
}

