#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;

  int x, y;
  int x_min = 10001, x_max = -10001;
  int y_min = 10001, y_max = -10001;

  for (int i = 0; i < N; i++) {
    cin >> x >> y;
    x_min = min(x_min, x);
    x_max = max(x_max, x);
    y_min = min(y_min, y);
    y_max = max(y_max, y);
  }

  int area = (x_max - x_min) * (y_max - y_min);
  cout << area << '\n';

  return 0;
}