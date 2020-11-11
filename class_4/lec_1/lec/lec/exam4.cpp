#include <iostream>
using namespace std;

int main() {
	char lowerCaseLetter, upperCaseLetter;
	int offset;
	cout << "Please input a lowerCaseLetter" << endl;
	cin >> lowerCaseLetter;
	offset = (int)(lowerCaseLetter - 'a');
	upperCaseLetter = offset + 'A';
	cout << "The loerCaseLetter of " << lowerCaseLetter << " is " << upperCaseLetter;
	return 0;
}