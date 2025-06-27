#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int arr[42] = {0};

  for (int i = 0; i < 10; i++) {
    int num;
    cin >> num;
    arr[num % 42] += 1;
  }

  int cnt = 0;
  for (int j = 0; j < 42; j++) {
    if (arr[j] != 0) cnt += 1;
  }

  cout << cnt << '\n';

  return 0;
}