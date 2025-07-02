#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, K, cnt = 0, result = 0;
  cin >> N >> K;

  for (int i = 1; i < N+1; i++) {
    if (N % i == 0) cnt++;
    if (cnt == K) {
      result = i;
      break;
    }
  }

  cout << result << '\n';

  return 0;
}