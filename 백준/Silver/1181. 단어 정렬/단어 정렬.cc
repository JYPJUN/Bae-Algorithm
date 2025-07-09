#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const string& a, const string& b) {
  if (a.length() != b.length()) return a.length() < b.length();
  return a < b;
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;
  vector<string> arr(N);
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end(), cmp);
  arr.erase(unique(arr.begin(), arr.end()), arr.end());

  for (int j = 0; j < arr.size(); j++) {
    cout << arr[j] << '\n';
  }

  return 0;
}