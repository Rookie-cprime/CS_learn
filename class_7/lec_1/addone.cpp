#include <iostream>
#include <vector>
using namespace std;

void addone(int *ptr);


int main()
{
    int *a;
    int b;
    b = 3;
    a = &b;
    addone(a);
    cout<<b<<endl;
    return 0;
}

void addone(int *ptr){
    *ptr = *ptr+1;
}
