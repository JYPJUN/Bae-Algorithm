#include <iostream>
#include <string>

using namespace std;

int main() {
	
	int a;
	cin >> a;

	for (int i = 1; i < a + 1; i++) {
		cout << string(a-i, ' ') << string(i, '*') << '\n';
	}
	
	return 0;
}