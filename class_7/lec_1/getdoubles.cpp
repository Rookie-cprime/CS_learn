#include <iostream>
using namespace std;
/**********************************
void getDouble(double *a){
    int i;
    for (i=1;i<=6;i++){
        a[i-1] = (double) i / 3 ;
    }
}


int main()
{
    double b [6];
    getDouble(b);
    int i ;
    for (i = 0;i<6;i++){
        cout << b[i] <<" ";
    }
    cout<<endl;
}
************************************/
double *getDouble(int doubleNums){
    double *a = new double [doubleNums];
    for(int i=0;i<doubleNums;i++){
        a[i] = (double)(i+1)/3;
    }
    return a;
}

int main(){
    double *b;
    b = getDouble(6);
    int i;
    for(i=0;i<6;i++){
        cout<<b[i]<<endl;
    }
    delete [] b;
    return 0;
}
