#include <iostream>
using namespace std;

bool arr[10001];

void _func() {
  fill(arr, arr+10001, true);
  arr[0] = arr[1] = false;

  for (int i = 2; i*i <= 10000; i++) {
    if (!arr[i]) continue;
    for (int j = i*i; j <= 10000; j += i) {
      if (arr[j]) {
        arr[j] = false;
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  _func();

  int M, N, min_val=0, total_sum = 0;
  cin >> M >> N;

  for (int i = M; i <= N; i++) {
    if (arr[i]) {
      if (min_val == 0) min_val = i;
      total_sum += i;
    }
  }
  if (min_val == 0) cout << -1 << '\n';
  else {
    cout << total_sum << '\n';
    cout << min_val << '\n';
  }
  

  return 0;
}