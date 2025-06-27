#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int max_val = 0, rank = 1;
  cin >> max_val;

  for (int i = 2; i < 10; i++) {
    int num;
    cin >> num;
    if (num > max_val) {
      max_val = num;
      rank = i;
    }
  }

  cout << max_val << '\n';
  cout << rank << '\n';

  return 0;
}