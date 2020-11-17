#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int total;
	int quarter, penny, dime, nickle, dollar,cent;
	cout << "Please enter the number of coins:" << endl;
	cout << "# of quarters:";
	cin >> quarter;
	cout << endl << "# of dimes:";
	cin >> dime;
	cout << "\n # of nickle:";
	cin >> nickle;
	cout << endl << "# of penny:";
	cin >> penny;
	cout << endl;
	total = 25 * quarter + 10 * dime + 5 * nickle + penny;
	dollar = total / 100;
	cent = total - dollar*100;
	cout << "the total is " << dollar << " dollars and " << cent << " cents" << endl;
}