#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  
  vector<bool> walls(N, false);

  for (int i = 0; i < M; ++i) {
    int x, y;
    cin >> x >> y;
    for (int j = x; j < y; ++j) {
      walls[j] = true;
    }
  }

  int remainWall = 0;
  for (int i = 1; i < N; ++i) {
    if (!walls[i]) {
      ++remainWall;
    }
  }

  cout << remainWall+1 << endl;

  return 0;
}