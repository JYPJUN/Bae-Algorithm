#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string arr[5];

  for (int i = 0; i < 5; i++) cin >> arr[i];

  for (int n = 0; n < 15; n++) {
    for (int m = 0; m < 5; m++) {
      if (n < arr[m].size()) {
      cout << arr[m][n];
      }
    }
  }

  return 0;
}