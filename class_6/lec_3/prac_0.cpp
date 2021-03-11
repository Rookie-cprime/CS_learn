#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    double cargo0,cargo1,tax_rate,base_price,after_discount,total_price;
    string club_card;
    cout<<"Enter price of the first item:";
    cin>>cargo0;
    cout<<"Enter price of the second item:";
    cin>>cargo1;
    cout<<"Does customer have a club card? (Y/N):";
    cin>>club_card;
    cout<<"Enter tax rate:";
    cin>>tax_rate;
    base_price = cargo0+cargo1;
    if (cargo0>cargo1)
        after_discount = cargo0+cargo1/2;
    else
        after_discount = cargo0/2+cargo1;
    if(club_card == "Y"||club_card == "y"||club_card == "yes")
        after_discount*=0.9;
    total_price = after_discount*tax_rate/100+after_discount;
    cout<<fixed<<setprecision(2)<<"Base base_price = "<<base_price<<endl;
    cout<<"Price after discounts = "<<after_discount<<endl;
    cout<<"Total price = "<<total_price<<endl;

}

