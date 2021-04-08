#include <iostream>
using namespace std;

void swap(int *a,int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void selection_sort(int *arr,int element){
    for (int i = 0;i<element-1;i++){
        for(int j = i;j<element;j++){
            if(arr[i]>arr[j])
                swap(&arr[i],&arr[j]);
        }
    }
}



int main()
{

    int lst[] = {19,2,20,1,0,18};
    selection_sort(lst,6);
    for(int i = 0;i<6;i++){
        cout<<lst[i]<<" ";
    }
    cout<<endl;
}

