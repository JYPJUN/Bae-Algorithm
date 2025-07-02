#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, s = 1, result = 1;
  cin >> N;

  while (result < N) {
    result += s * 6;
    s += 1;
  }

  cout << s << '\n';
  
  return 0;
}