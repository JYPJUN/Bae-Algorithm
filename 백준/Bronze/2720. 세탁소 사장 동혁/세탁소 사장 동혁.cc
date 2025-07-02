#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    int C, a = 0, b = 0, c = 0, d = 0;
    cin >> C;

    a = C / 25;
    C %= 25;
    b = C / 10;
    C %= 10;
    c = C / 5;
    d = C % 5;

    cout << a << ' ' << b << ' ' << c << ' ' << d << '\n';
  }

  return 0;
}