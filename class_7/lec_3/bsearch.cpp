#include <iostream>
using namespace std;

int binary_search(int search_value,int lst[],int elements){
    int low = 0;
    int up = elements-1;
    int times = 0;
    int mid;
    bool found = false;
    while(low <= up){
        times++;
        mid = (low+up)/2;
        if(lst[mid] == search_value){
            return mid+1;
        }
        else if(lst[mid]>search_value)
            up = mid-1;
        else 
            low = mid+1;
    }
    return times;
}

int main()
{
    int lst[] = {0,1,2,18,19,20,25};
    cout << binary_search(20,lst,7)<<endl;
    cout << binary_search(28,lst,7)<<endl;
    return 0;
}

