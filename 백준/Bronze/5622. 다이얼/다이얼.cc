#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int time[26] = {3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};

  string s;
  cin >> s;
  int result = 0;
  for (int i = 0; i < s.size(); i++) result += time[s[i] - 'A'];
  cout << result << '\n';

  return 0;
}