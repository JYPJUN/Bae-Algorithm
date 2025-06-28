#include <iostream>
#include <string>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  string line;
  int cnt = 0;
  getline(cin, line);

  bool flag = false;

  for (int i = 0; i < line.size(); i++) {
    if (!flag && line[i] != ' ') {
      cnt++;
      flag = true;
    }
    if (flag && line[i] == ' ') flag = false;
  }

  cout << cnt << '\n';

  return 0;
}