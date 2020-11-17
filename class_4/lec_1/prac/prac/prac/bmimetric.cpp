#include<iostream>
#include<cmath>
using namespace std;

int main() {
	float ibm;
	float result;
	float weight, height;
	cout << "Please  enter weight  in  kilograms: ";
	cin >> weight;
	cout << "Please  enter height  in  meters:";
	cin >> height;
	ibm = weight / (height *height);
	ibm = ibm * 100;
	ibm = int(ibm+0.5);
	ibm = float(ibm) / 100;

	cout << "BMI is: " << ibm;
	return 0;

}