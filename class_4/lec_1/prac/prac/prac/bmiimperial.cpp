#include<iostream>
#include<cmath>
using namespace std;

int main() {
	float ibm;
	float pound, inche;
	double weight, height;
	cout << "Please  enter weight  in  pound: ";
	cin >> pound;
	weight = pound * 0.453592;
	cout << "Please  enter height  in  inche:";
	cin >> inche;
	height = inche * 0.0254;
	ibm = weight / (height * height);
	ibm = ibm * 100;
	ibm = int(ibm + 0.5);
	ibm = float(ibm) / 100;

	cout << "BMI is: " << ibm;
	return 0;

}