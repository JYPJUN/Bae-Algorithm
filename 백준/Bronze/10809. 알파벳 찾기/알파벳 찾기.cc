#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string word;
  cin >> word;

  int words[26];
  for (int i = 0; i < 26; i++) words[i] = -1;

  for (int i = 0; i < word.size(); i++) {
    if (words[word[i] - 'a'] == -1) words[word[i] - 'a'] = i;
  }

  for (int j = 0; j < 26; j++) {
    cout << words[j] << ' ';
  }

  return 0;
}