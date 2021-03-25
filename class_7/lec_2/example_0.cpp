#include <iostream>
using namespace std;

void printAsc(int start,int end){
    if(start == end)
        cout<<start<<endl;
    else{
        cout<<start<<endl;
        printAsc(++start,end);
    }
}


int main()
{
    printAsc(1,5);
}

