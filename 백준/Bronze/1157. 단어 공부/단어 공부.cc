#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string word;
  cin >> word;

  int arr[26] = {0};
  for (int i = 0; i < word.size(); i++) {
    if (word[i] < 'a') arr[word[i]-'A'] += 1;
    else arr[word[i]-'a'] += 1;
  }

  int cnt = -1;
  char result;
  for (int j = 0; j < 26; j++) {
    if (arr[j] > cnt) {
      cnt = arr[j];
      result = j + 'A';
    } else if (arr[j] == cnt) {
      result = '?';
    }
  }

  cout << result << '\n';

  return 0;
}