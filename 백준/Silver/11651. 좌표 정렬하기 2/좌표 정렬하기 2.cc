#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Data {
  int x, y;
};

bool cmp(const Data& a, const Data& b) {
  if (a.y != b.y) return a.y < b.y;
  return a.x < b.x;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;
  vector<Data> arr(N);
  for (int i = 0; i < N; i++) {
    cin >> arr[i].x >> arr[i].y;
  }

  sort(arr.begin(), arr.end(), cmp);
  
  for (int i = 0; i < N; i++) {
    cout << arr[i].x << ' ' << arr[i].y << '\n';
  }

  return 0;
};
