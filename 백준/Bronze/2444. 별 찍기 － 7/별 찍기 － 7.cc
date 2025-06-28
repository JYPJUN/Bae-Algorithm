#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin >> n;

  for (int i = 1; i <= n; i++) {
    cout << string(n-i, ' ');
    cout << string(2*i-1, '*') << '\n';
  }

  for (int i = n-1; i >=1; i--) {
    cout << string(n-i, ' ');
    cout << string(2*i-1, '*') << '\n';
  }

  return 0;
}