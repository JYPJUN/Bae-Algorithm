#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, min_v = 1000000, max_v = -1000000;
  cin >> N;

  for (int i = 0; i < N; i++) {
    int num;
    cin >> num;
    if (num < min_v) min_v = num;
    if (num > max_v) max_v = num;
  }

  cout << min_v << ' ' << max_v << '\n';

  return 0;
}