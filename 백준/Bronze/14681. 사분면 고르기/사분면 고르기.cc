#include <iostream>

using namespace std;

int main() {
	int a, b;
	cin >> a;
	cin >> b;

	if (a > 0) {
		if (b > 0) {
			cout << 1 << endl;
		}
		else {
			cout << 4 << endl;
		}

	}
	else {
		if (b > 0) {
			cout << 2 << endl;
		}
		else
			cout << 3 << endl;
	}

	return 0;
}
