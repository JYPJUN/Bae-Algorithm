#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int a, b, c;
  cin >> a >> b >> c;

  int total_time, sum_time;

  total_time = a * 60 + b;
  sum_time = total_time + c;

  a = sum_time / 60;
  b = sum_time % 60;

  if (a >= 24) a -= 24;

  cout << a << " " << b;

  return 0;
}