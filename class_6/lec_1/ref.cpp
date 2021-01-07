#include <iostream>
using namespace std;

void analyzeDigits(int num,int& outsum,int& digitnum){
    int remain;
    while(num != 0){
        remain =num- (num/10)*10;
        num /= 10;
        outsum+=remain;
        ++digitnum;
    }
}

int main()
{
    int num,outsum,digitnum;
    outsum = 0;
    digitnum = 0;
    cout << "Please input a integer" << endl;
    cin >> num;
    analyzeDigits(num,outsum,digitnum);
    cout <<"The digit num is "<<digitnum<<" The outsum is "<<outsum<<endl;
    return 0;
}

