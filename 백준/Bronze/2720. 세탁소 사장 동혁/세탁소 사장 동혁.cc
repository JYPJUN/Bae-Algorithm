#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  cin >> T;
  int coin[4] = {25, 10, 5, 1};

  for (int i = 0; i < T; i++) {
    int C;
    cin >> C;

    for (int i = 0; i < 4; i++) {
      cout << C / coin[i] << ' ';
      C %= coin[i];
    }
    cout << '\n';
  }

  return 0;
}