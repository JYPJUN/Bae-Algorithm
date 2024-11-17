#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FASTIO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define SETPRECISION(n) cout << fixed;cout.precision(n);
#define SIZE(v) (int)v.size()
#define ALL(v) v.begin(),v.end()

int main() {
	FASTIO;

	int n = 9;
	int num = 0, new_num = 0;
	int m = 1;

	for (int i = 0; i < n; i++) {
		cin >> new_num;
		if (new_num > num) {
			num = new_num;
			m = i+1;
		}
	}

	cout << num << '\n';
	cout << m << '\n';

	return 0;
}
