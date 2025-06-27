#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M;
  cin >> N >> M;

  int arr[101];

  for (int i = 1; i <N+1; i++) {
    arr[i] = i;
  }

  for (int m = 0; m < M; m++) {
    int i, j;
    cin >> i >> j;

    while (i < j) {
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
      i++;
      j--;
    }
  }

  for (int i = 1; i <= N; i++) {
    cout << arr[i] << ' ';
  }

  return 0;
}