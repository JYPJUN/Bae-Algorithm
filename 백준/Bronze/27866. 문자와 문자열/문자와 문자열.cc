#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string word;
  int n;
  cin >> word >> n;

  cout << word[n-1] << '\n';

  return 0;
}