#include <iostream>
using namespace std;

void swap(int *a,int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}


int main()
{
    int lst[] = {19,2,20};
    swap(&lst[0],&lst[1]);
    cout<<lst[0]<<" "<<lst[1]<<endl;
}

