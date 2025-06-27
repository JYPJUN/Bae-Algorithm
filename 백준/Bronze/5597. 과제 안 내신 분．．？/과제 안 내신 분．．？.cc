#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int arr[31] = {0};

  for (int i = 0; i < 28; i++) {
    int num;
    cin >> num;
    arr[num] += 1;
  }

  for (int j = 1; j < 31; j++) {
    if (arr[j] == 0) cout << j << '\n';
  }

  return 0;
}