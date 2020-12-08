#include <iostream>
using namespace std;

int main()
{
    float grade1,grade2;
    cout<<"Please enter 2 grades, separated by a space:";
    cin>>grade1>>grade2;
    cout<<grade1<<grade2<<endl;

    if(grade1 >= 60 && grade2>=60)
        cout<<"Student Graduated with Honors:)"<<endl;
    else if(grade1 < 60 && grade2 <= grade2<60)
        cout<<"Student Graduated!"<<endl;
    else
        cout<<"Student Failed:("<<endl;
    return 0;
}
