#include <iostream>
using namespace std;

string reverse_str(string word) {
  int i = 0, j = word.size()-1;

  while (i < j) {
    char temp;
    temp = word[i];
    word[i] = word[j];
    word[j] = temp;
    i++;
    j--;
  }

  return word;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string a_num, b_num;
  cin >> a_num >> b_num;

  a_num = reverse_str(a_num);
  b_num = reverse_str(b_num);

  cout << (a_num > b_num ? a_num : b_num) << '\n';

  return 0;
}

