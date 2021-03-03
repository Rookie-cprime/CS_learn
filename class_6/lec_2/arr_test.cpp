#include <iostream>
using namespace std;
const int MAX_CLASS_SIZE = 60;

int main()
{
    int gradesList [MAX_CLASS_SIZE];
    int currGrade;
    int ind;
    int numOfStudents;
    int sum;
    double average;
    int jnd;
    cout<<"Please enter the number of students in the class (no more than "<<MAX_CLASS_SIZE<<")"<<endl;
    cin>>numOfStudents;

    for (ind = 0;ind<numOfStudents;ind++){
        cin>>currGrade;
        gradesList[ind]=currGrade;
    }

    sum = 0;
    for (ind = 0;ind<numOfStudents;ind++){
        sum+=gradesList[ind];
    }

    average = (double)sum/(double)numOfStudents;
    cout<<"The class average is"<<average<<endl;

    cout<<"The grades above the average"<<endl;
    for(ind = 0;ind<numOfStudents;ind++){
        if(gradesList[ind]>average){
            cout<<gradesList[ind]<<" ";
        }
    }
    cout<<endl;
    return 0;
}

