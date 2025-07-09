#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;
  vector<int> arr(N);
  for (int i =0; i < N; i++) {
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  for (int j = 0; j < N; j++) {
    cout << arr[j] << '\n';
  }

  return 0;
}