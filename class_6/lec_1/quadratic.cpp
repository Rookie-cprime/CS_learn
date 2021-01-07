#include <iostream>
#include<cmath>
using namespace std;

const int NO_SOLUTION = 0;
const int ONE_REAL_SOLUTION = 1;
const int TWO_REAL_SOLUTION = 2;
const int ALL_REALS = 3;
const int NO_REAL_SOLUTION = 4;

int quadratic(double a,double b,double c,double& outX1,double& outX2);

int main(){
    double a,b,c,x1,x2;
    cout<<"Please enter coefficients of quadratic equation:\n"<<endl;
    cin>>a>>b>>c;
    cout<<"The equation:"<<a<<"x^2+ "<<b<<"x+ "<<c<<" = 0"<<endl;
    switch(quadratic(a,b,c,x1,x2)){
        case TWO_REAL_SOLUTION:
            cout<<"Solution: "<<x1<<" "<<x2<<endl;break;
        case ONE_REAL_SOLUTION:
            cout<<"Solution: "<<x1<<endl;break;
        case NO_REAL_SOLUTION:
            cout<<"No real solution"<<endl;break;
        case NO_SOLUTION:
            cout<<"No Solution"<<endl;break;
        case ALL_REALS:
            cout<<"All real number are solution"<<endl;break;
        default:
            cout<<"ERROR"<<endl;break;
    }
    return 0;
}

int quadratic(double a,double b,double c,double& outX1,double& outX2){
    double delta;
    if(a!=0.0){
        delta = b*b - 4*a*c;
        if(delta>0){
            outX1 = (sqrt(delta)-b)/(2*a);
            outX2 = (-sqrt(delta)-b)/(2*a);
            return TWO_REAL_SOLUTION;
        }
        else if(delta==0){
            outX1 = -b/(2*a);
            return ONE_REAL_SOLUTION;
        }
        else
            return NO_REAL_SOLUTION;
    }
    else{
        if(b!=0.0){
            outX1 = -c/b;
            return ONE_REAL_SOLUTION;
        }
        else if(c!=0.0)
            return NO_SOLUTION;
        else
            return ALL_REALS;
    }
}

