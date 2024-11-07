#include <iostream>

using namespace std;

int main() {
	int allPrice;
	cin >> allPrice;

	int a;
	int sumPrice = 0;
	cin >> a;

	for (int i = 0; i < a; i++) {
		int x, y;
		cin >> x >> y;
		sumPrice += x * y;
	}

	if (sumPrice == allPrice) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
	
	return 0;
}
