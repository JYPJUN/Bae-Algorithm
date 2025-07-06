#include <iostream>
#include <vector>
using namespace std;

char color_find(int row, int col, bool start) {
  if ((row + col) % 2 == 0) {
    return start ? 'W' : 'B';
  } else {
    return start ? 'B' : 'W';
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, M;
  cin >> N >> M;
  vector<string> board(N);
  for (int i = 0; i < N; i++) {
    cin >> board[i];
  }

  int result = 64;

  for (int i = 0; i <= N-8; i++) {
    for (int j = 0; j <= M-8; j++) {
      int re_w = 0;
      int re_b = 0;

      for (int r = 0; r < 8; r++) {
        for (int c = 0; c < 8; c++) {
          char actual = board[i+r][j+c];

          if (actual != color_find(r, c, true)) re_w++;

          if (actual != color_find(r, c, false)) re_b++;
        }
      }

      result = min(result, min(re_w, re_b));
    }
  }

  cout << result << '\n';

  return 0;
}