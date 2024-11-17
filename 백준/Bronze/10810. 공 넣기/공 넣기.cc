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

	int N, M, i, j, k;
	cin >> N >> M;

	vector<int> arr(N, 0);
	for (int a = 0; a < M; a++) {
		cin >> i >> j >> k;
		for (int b = i - 1; b < j; b++) {
			arr[b] = k;
		}
	}
	
	for (int i = 0; i < N; i++) {
		cout << arr[i];
		if (i != N - 1) cout << " ";
	}
	cout << '\n';

	return 0;
}
