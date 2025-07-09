#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int arr[5], mean_sum = 0;

  for (int i = 0; i < 5; i++) {
    cin >> arr[i];
    mean_sum += arr[i];
  }

  sort(arr, arr+5);

  cout << mean_sum / 5 << '\n';
  cout << arr[2] << '\n';

  return 0;
}