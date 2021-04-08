#include <iostream>
using namespace std;

int linear_search(int search_value,int lst[],int elements){
    int temp = 0;
    for(int i = 0;i<elements;i++){
        if(search_value == lst[i])
            return i+1;
        else{
            if(lst[i]>temp)
                temp = lst[i];
        }
    }
    return temp;
}

int main()
{
    int lst[] = {19,2,20,1,0,18};

    cout <<linear_search(20,lst,6) << endl;
    return 0;
}

