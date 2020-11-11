#include<iostream>
#include<cmath>
using namespace std;
int main2() {
	double radius, area;
	cout << "Please enter the radius" << endl;
	cin >> radius;
	area = 3.14 * (radius * radius);
	cout << "The result = " << area;
	return 0;
}