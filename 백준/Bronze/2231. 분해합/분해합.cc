#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int get_digit(int num) {
  int sum = num;

  while (num > 0) {
    sum += num % 10;
    num /= 10;
  }

  return sum;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;
  int digit_len = to_string(N).length();
  int s = max(1, N - 9 * digit_len);

  int result = 0;
  for (int i = s; i < N; i++) {
    if (get_digit(i) == N) {
      result = i;
      break;
    }
  }

  cout << result << '\n';

  return 0;
}