#include <iostream>
#include <functional>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string num;
  cin >> num;
  vector<char> arr;
  for (int i = 0; i < num.length(); i++) {
    arr.push_back(num[i]);
  }

  sort(arr.begin(), arr.end(), greater<char>());

  for (int j = 0; j < num.length(); j++) {
    cout << arr[j];
  }

  return 0;
}