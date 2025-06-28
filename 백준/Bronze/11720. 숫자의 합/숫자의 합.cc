#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N, result=0;
  cin >> N;

  string word;
  cin >> word;

  for (int i = 0; i < N; i++) {
    result += word[i] - '0';
  }

  cout << result << '\n';

  return 0;
}