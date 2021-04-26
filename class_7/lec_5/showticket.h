#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class ShowTicket
{
private:
    string seat_num;
    string state,row;
public:
    ShowTicket(string row = "AA",string seat_num = "000"){
        this->row = row;
        this->seat_num = seat_num;
        this->state = "available";
    }
    bool is_sold(){
        if(this->state == "available")
            return false;
        else
            return true;
    }
    void sell_seat(){
        if(!is_sold())
            this->state = "sold";
        else
            cout<<"THIS TICKET HAS BEEN SOLD"<<endl;
    }
    void set_row(string row){
        this->row = row;
    }
    void set_seat(string seat){
        seat_num = seat;
    }
   virtual string print_ticket(){
        return row+" "+seat_num+" "+state;
    }
    string get_seat(){
        return seat_num;
    }
    string get_row(){
        return row;
    }
};

class ShowTickets{
private:
    ShowTicket pack[10];
public:
    ShowTickets(){
    for(int i = 0;i<10;i++){
       string c;
       stringstream ss;
        ss << 101+i;
        ss >> c;
       pack[i].set_row("AA");
       pack[i].set_seat(c);
    }
    }

  int _fund(string row,string seat){
        for(int i = 0;i<10;i++){
            if((row == pack[i].get_row())&&(seat == pack[i].get_seat()))
                return i;
        }
        return -1;
    }

  bool is_sold(string row,string seat){
      int j = this->_fund(row,seat);
      if(j>=0)
       return pack[j].is_sold();
      else{
          cout<<"NO THIS TICKETS"<<endl;
          return false;  
      }
  }
  void sell_seat(string row,string seat){
      int j = this->_fund(row,seat);
      if(j>=0)
          pack[j].sell_seat();
      else
          cout<<"NO THIS TICKETS"<<endl; 
      }
  string print_ticket(string row,string seat){
      int j = this->_fund(row,seat);
      if(j>=0)
       return pack[j].print_ticket();
      else
          return "NO THIS TICKETS\n"; 
  }

};

class SportTicket:public ShowTicket{
private:
    bool beer;
public:
    SportTicket(string row,string seat){
        ShowTicket(row,seat);
        this->beer = false;
    }

    bool bear_sold(){
        return beer;
    }

    void sell_beer(){
        if(!this->bear_sold())
            beer = true;
        else
            cout<<"THIS HAS BEER"<<endl;
    }
    string print_ticket(){
        string c = (bear_sold())?"beer":"nobeer";
        string b = (is_sold())?"sold":"available";
        return  get_row() + " " + get_seat() + " " + b + " " + c;
    }
};
