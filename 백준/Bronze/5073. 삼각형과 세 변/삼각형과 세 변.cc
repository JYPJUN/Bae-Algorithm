#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int x, y, z;

  while (cin >> x >> y >> z) {
    if (x == 0 && y == 0 && z == 0) {
      break;
    }

    if (x+y+z - (2*max({x, y, z})) <= 0) {
      cout << "Invalid" << '\n';
      continue;
    }

    if (x == y && y == z) {
      cout << "Equilateral" << '\n';
    }
    else if (x == y || y == z || x == z) {
      cout << "Isosceles" << '\n';
    }
    else {
      cout << "Scalene" << '\n';
    }
  }

  return 0;
}