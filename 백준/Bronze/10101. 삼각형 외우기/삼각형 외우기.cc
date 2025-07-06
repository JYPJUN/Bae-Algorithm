#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int x, y, z;
  cin >> x >> y >> z;
  
  if (x + y + z != 180) {
    cout << "Error" << '\n';
  }
  else if (x == y && y == z) {
    cout << "Equilateral" << '\n';
  }
  else if (x == y || x == z || y == z) {
    cout << "Isosceles" << '\n';
  }
  else {
    cout << "Scalene" << '\n';
  }

  return 0;
}