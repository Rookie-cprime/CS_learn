#include <iostream>
using namespace std;

int maxinlst(int lst[],int size){
    int max_value;
    int i;
    max_value = lst[0];
    for(i=1;i<size;i++){
        if(lst[i]>max_value)
            max_value = lst[i];
    }
    return max_value;
}

int maxabsinlst(int lst[],int size){
    int max_value;
    int i;
    for(i=0;i<size;i++){
        if(lst[i]<0)
            lst[i] = -lst[i];
    }
    max_value = lst[0];
    for(i=1;i<size;i++){
        if(lst[i]>max_value)
            max_value = lst[i];
    }
    return max_value;
}

double avgoflst(int lst[],int size){
    int sum;
    double average;
    int i;
    sum = 0;
    for(i=0;i<size;i++){
        sum += lst[i];
    }
    average = (double)sum/(double)size;
    return average;

}


int main()
{
   int lis[] = {-19,-3,20,-1,5,-25};
    cout<<maxinlst(lis,6)<<endl;
    cout<<maxabsinlst(lis,6)<<endl;
    cout<<avgoflst(lis,6)<<endl;
}

