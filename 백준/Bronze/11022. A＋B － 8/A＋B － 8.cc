#include <iostream>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int a, b, c;
	cin >> a;

	for (int i = 0; i < a; i++) {
		cin >> b >> c;
		cout << "Case #" << i + 1 << ": " << b << " + " << c << " = " << b + c << '\n';
	}

	return 0;
}