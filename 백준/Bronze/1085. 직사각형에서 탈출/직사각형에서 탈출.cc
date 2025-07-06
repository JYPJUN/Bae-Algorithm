#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int x, y, w, h;
  cin >> x >> y >> w >> h;

  int x_num = x < w-x ? x : w-x;
  int y_num = y < h-y ? y : h-y;
  
  cout << (x_num < y_num ? x_num : y_num) << '\n';

  return 0;
}