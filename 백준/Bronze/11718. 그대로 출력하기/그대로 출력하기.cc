#include <iostream>
#include <string>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string word;
  
  while (getline(cin, word)) {
    cout << word << '\n';
  }

  return 0;
}