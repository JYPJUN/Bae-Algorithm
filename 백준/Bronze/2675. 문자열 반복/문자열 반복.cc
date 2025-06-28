#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    int cnt;
    string word;
    cin >> cnt >> word;

    string result = "";

    for (int j = 0; j < word.size(); j++) {
      result += string(cnt, word[j]);
    }

    cout << result << '\n';
  }

  return 0;
}