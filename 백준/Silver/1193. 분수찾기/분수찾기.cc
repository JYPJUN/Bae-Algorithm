#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int X, cnt = 1, s = 2;
  cin >> X;

  while (cnt < X) {
    cnt += s;
    s += 1;
  }
  s -= 1;
  cnt -= s;
  X -= cnt;

  if (s % 2 == 0) {
    cout << X << '/' << s - X + 1 << '\n';
  } else {
    cout << s - X +1 << '/' << X << '\n';
  }

  return 0;
}