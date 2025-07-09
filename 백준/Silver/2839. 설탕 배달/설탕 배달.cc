#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;

  vector<int> dp(N+1, 1e9);
  dp[0] = 0;

  for (int i = 1; i <= N; i++) {
    if  (i >= 3) {
      dp[i] = min(dp[i], dp[i-3] + 1);
    }
    if (i >= 5) {
      dp[i] = min(dp[i], dp[i-5] + 1);
    }
  }

  if (dp[N] == 1e9) cout << -1 << '\n';
  else cout << dp[N] << '\n';

  return 0;
}