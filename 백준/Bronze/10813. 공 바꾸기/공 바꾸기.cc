#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M;
  cin >> N >> M;

  int arr[100] = {0};
  for (int i = 0; i < N; i++) arr[i] = i+1;

  for (int j = 0; j < M; j++) {
    int temp, a, b;
    cin >> a >> b;

    temp = arr[a-1];
    arr[a-1] = arr[b-1];
    arr[b-1] = temp;
  }

  for (int k=0; k <N; k++) cout << arr[k] << ' ';

  return 0;
}