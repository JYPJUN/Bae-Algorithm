#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  bool arr[100][100] = {0};
  int sum = 0;
  int n; cin >> n;

  while (n--) {
    int x, y;
    cin >> x >> y;
    for (int i = y; i < y+10; i++) {
      for (int j= x; j < x+10; j++) {
        if (arr[i][j]) continue;
        arr[i][j] = 1;
        sum ++;
      }
    }
  }

  cout << sum;

  return 0;
}