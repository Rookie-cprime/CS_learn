#include <iostream>
using namespace std;


void merge(int arr[],int left,int middle,int right){
    int lstart,rstart,lenth,i;
    lstart = left;
    rstart = middle+1;
    lenth = right - left + 1;
    i = 0;
    int *lst = new int [lenth];
    while(true){
        if(lstart > middle || rstart > right)
            break;
        if(arr[lstart]<arr[rstart]){
            lst[i++] = arr[lstart];
            lstart++;
        }
        else{
            lst[i++] = arr[rstart];
            rstart++;
        }
        
    }
    if(lstart > middle){
        while(true){
            if(rstart > right)
                break;
            lst[i++] = arr[rstart++];
        }
    }
    else{
        while(true){
            if(lstart > middle)
                break;
            lst[i++] = arr[lstart++];

        }
    }
    for(int j = 0;j<lenth;j++){
        arr[left++] = lst[j];
    }
    delete [] lst;
}


int main()
{
    int lst[] = {0,2,1,18,20};
    merge(lst,0,1,4);
    for(int i = 0;i<5;i++){
        cout<<lst[i]<<" ";
    }
    cout<<endl;
}

