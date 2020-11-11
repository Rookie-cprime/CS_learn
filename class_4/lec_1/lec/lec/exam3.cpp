#include<iostream>
using namespace std;

int main() {
	char inputChar;
	int asciiValue;

	cout << "Please enter a character:" << endl;
	cin >> inputChar;
	asciiValue = (int)inputChar;
	cout << "The ascii calue of" << inputChar << "is" << asciiValue;
	return 0;
}