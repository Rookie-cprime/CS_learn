#include <iostream>
#include <string>
using namespace std;


int main()
{
    int star_time;
    int total_time;
    double price,cost;
    string day;
    cout<<"Enter the day the call started at:";
    cin>>day;
    cout<<"Enter the time the call started at (hhmm):";
    cin>>star_time;
    cout<<"Enter the duration of the call (in minutes):";
    cin>>total_time;
    if(day == "Sat"||day == "Sun"){
        price = 0.15;
    }
    else{
        if(star_time<=1800&&star_time>=800)
            price = 0.4;
        else
            price = 0.25;
    }

    cost = double(total_time)*price;
    cout<<"This call will cost $"<<cost<<endl;
    

}

