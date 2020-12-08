#include <iostream>
using namespace std;

int main()
{
    int num1,num2,num3,num4;
    int oddcnt,evencnt;
    oddcnt = 0;
    evencnt = 0;
    cout << "Please enter 4 positive integers, separated by a space:";
    cin>>num1>>num2>>num3>>num4;
    if (num1%2 == 0)
        evencnt += 1;
    else
        oddcnt += 1;

    if (num2%2 == 0)
        evencnt += 1;
    else
        oddcnt += 1;

    if (num3%2 == 0)
        evencnt += 1;
    else
        oddcnt += 1;

    if (num4%2 == 0)
        evencnt += 1;
    else
        oddcnt += 1;

    if(oddcnt > evencnt)
        cout<<"more odds"<<endl;
    else if(oddcnt<evencnt)
        cout<<"more evens"<<endl;
    else
        cout<<"same number of evens and odds"<<endl;

    return 0;
}

