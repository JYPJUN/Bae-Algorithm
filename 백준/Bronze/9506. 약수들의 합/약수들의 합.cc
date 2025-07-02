#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  while (true) {
    int n;
    cin >> n;
    if (n == -1) break;

    vector<int> arr;
    int sum = 0;

    for (int i = 1; i < n; i++) {
      if (n % i == 0) {
        arr.push_back(i);
        sum += i;
      }
    }

    if (sum == n) {
      cout << n << " = ";
      for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i != arr.size() - 1) cout << " + ";
      }
      cout << '\n';
    } else {
      cout << n << " is NOT perfect." << '\n';
    }
  }

  return 0;
}