#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string word;
  cin >> word;
  int i=0, j = word.size()-1;
  bool flag = true;
  while (i < j) {
    if (word[i] != word[j]) {
      flag = false;
      break;
    }
    i++;
    j--;
  }

  cout << flag << '\n';

  return 0;
}