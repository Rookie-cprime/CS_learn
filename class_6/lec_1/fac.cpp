#include <iostream>
using namespace std;

int factorial(int num);

int main()
{   
    int n,k,i,nFact,kFact,n_kFact,k_comb;
    cout << "Please enter n and k(n>=k):" << endl;
    cin >> n>>k;
    nFact = factorial(n);
    kFact = factorial(k);
    n_kFact = factorial(n-k);
    k_comb = nFact/(kFact*n_kFact);
    cout<<"The n to k is: "<<k_comb;
    
    return 0;
}

int factorial (int num){
    int factRes,i;
    factRes = 1;
    for(i=1;i<=num;i++)
        factRes*=i;
    return factRes;
}
