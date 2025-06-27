#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M;
  cin >> N >> M;

  vector<int> arr(N, 0);

  for (int m = 0; m < M; m++) {
    int i, j, k;
    cin >> i >> j >> k;

    for (int n = i-1; n < j; n++) {
      arr[n] = k;
    }
  }

  for (int p = 0; p < N; p++) {
    cout << arr[p] << ' ';
  }

  return 0;
}