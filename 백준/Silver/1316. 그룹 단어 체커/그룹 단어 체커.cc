#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, result = 0;
  cin >> N;

  for (int i = 0; i < N; i++) {
    string word;
    cin >> word;

    bool visited[26] = {false};
    bool isGroup = true;
    char prev = 0;

    for (int j = 0; j < word.size(); j++) {
      if (word[j] != prev) {
        if (visited[word[j] - 'a']) {
          isGroup = false;
          break;
        }
        visited[word[j]-'a'] = true;
      }
      prev = word[j];
    }
    if (isGroup) result++;
  }

  cout << result << '\n';

  return 0;
}