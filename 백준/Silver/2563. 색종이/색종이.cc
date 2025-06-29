#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, total_cnt = 0;
  cin >> N;
  bool arr[101][101] = {false};

  for (int i = 0; i < N; i++) {
    int left, bottom;
    cin >> left >> bottom;

    for (int p = left; p < left+10; p++) {
      for (int q = bottom; q < bottom+10; q++) {
        arr[p][q] = true;
      }
    }
  }

  for (int n = 0; n < 100; n++) {
    for (int m = 0; m < 100; m++) {
      total_cnt += arr[n][m];
    }
  }

  cout << total_cnt << '\n';

  return 0;
}