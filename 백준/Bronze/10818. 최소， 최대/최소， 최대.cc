#include <iostream>
using namespace std;

#define FASTIO ios_base::sync_with_stdio(false);cin.tie(NULL);
#define SETPRECISION(n) cout << fixed;cout.precision(n);
#define SIZE(v) (int)v.size()
#define ALL(v) v.begin(),v.end()

int main() {
	FASTIO;

	int n, num =0;
	int max_num = -1000000;
	int	min_num = 1000000;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> num;
		if (num < min_num) {
			min_num = num;
		}
		if (num > max_num) {
			max_num = num;
		}
	}
	cout << min_num << " " << max_num << '\n';

	return 0;
}
