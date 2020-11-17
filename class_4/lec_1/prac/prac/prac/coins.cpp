#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int quarter, dime, nickle, penny;
	int total, dollar, cent;
	cout << "Please enter the amount of money to convert:" << endl;
	cout << "# of dollars:";
	cin >> dollar;
	cout << "# of cents:";
	cin >> cent;
	total = 100 * dollar + cent;
	quarter = total / 25;
	total = total - quarter * 25;
	dime = total / 10;
	total = total-10*dime;
	nickle = total / 5;
	penny = total - 5 * nickle;
	cout << "The coins are " << quarter << " quarters, " << dime << " dimes, " << nickle << " nickles and " << penny << "pennies." << endl;
		return 0;
}
