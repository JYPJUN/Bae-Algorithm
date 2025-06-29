#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int arr[9][9];
  int max_num = -1, n, m;

  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cin >> arr[i][j];
      if (arr[i][j] > max_num) {
        max_num = arr[i][j];
        n = i;
        m = j;
      }
    }
  }

  cout << max_num << '\n' << n+1 << ' ' << m+1 << '\n';

  return 0;
}