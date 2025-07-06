#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int a, b, c, result;
  cin >> a >> b >> c;
  result = a + b + c;

  int max_leng = max({a, b, c});
  if (a+b+c - 2*max_leng <= 0) {
    result -= max_leng;
    max_leng = a+b+c - max_leng - 1;
    result += max_leng;
  }

  cout << result << '\n';

  return 0;
}