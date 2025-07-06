#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M, max_num = 0;
  cin >> N >> M;
  vector<int> arr(N);
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  
  for (int a = 0; a < N; a++) {
    for (int b = a+1; b < N; b++) {
      for (int c = b+1; c < N; c++) {
        int sum = arr[a] + arr[b] + arr[c];
        if (sum <= M) {
          max_num = max({max_num, sum});
        }
      }
    }
  }

  cout << max_num << '\n';

  return 0;
}