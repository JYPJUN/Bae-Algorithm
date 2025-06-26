#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int a, b;
  cin >> a >> b;

  int b1 = b % 10;
  int b2 = (b / 10) % 10;
  int b3 = b / 100;

  cout << a * b1 << endl;
  cout << a * b2 << endl;
  cout << a * b3 << endl;
  cout << a * b << endl;

  return 0;
}