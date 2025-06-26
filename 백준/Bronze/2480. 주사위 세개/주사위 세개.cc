#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int a, b, c;
  cin >> a >> b >> c;

  int prize = 0;

  if (a == b && b == c) {
    prize = 10000 + a*1000;
  } else if (a == b || a == c) {
    prize = 1000 + a * 100;
  } else if (b == c) {
    prize = 1000 + b * 100;
  } else {
    prize = max({a, b, c}) * 100;
  }

  cout << prize << endl;

  return 0;
}