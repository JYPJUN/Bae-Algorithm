#include <iostream>
#include <cmath>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;

  int side = pow(2, N) + 1;
  int result = side * side;

  cout << result << '\n';

  return 0;
}