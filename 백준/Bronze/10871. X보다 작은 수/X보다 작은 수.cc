#include <iostream>
using namespace std;

#define FASTIO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define SETPRECISION(n) cout << fixed;cout.precision(n);
#define SIZE(v) (int)v.size()
#define ALL(v) v.begin(),v.end()
using ll = long long;

int main() {
	FASTIO;

	int n, x;
	cin >> n >> x;

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;

		if (num < x) {
			cout << num << ' ';
		}
	}

	return 0;
}
