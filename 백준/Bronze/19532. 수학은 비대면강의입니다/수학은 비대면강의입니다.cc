#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;

  int div = a * e - d * b;
  int x_num = c * e - f * b;
  int y_num = a * f - d * c;

  int x = x_num / div;
  int y = y_num / div;

  cout << x << ' ' << y << '\n';

  return 0;
}