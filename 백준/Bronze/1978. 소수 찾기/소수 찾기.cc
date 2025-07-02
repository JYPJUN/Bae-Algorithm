#include <iostream>
using namespace std;

bool isPrime[1001];

void sieve() {
  fill(isPrime, isPrime + 1001, true);
  isPrime[0] = isPrime[1] = false;

  for (int i = 2; i * i <= 1000; i++) {
    if (isPrime[i]) {
      for (int j = i * i; j <= 1000; j += i) {
        isPrime[j] = false;
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  sieve();

  int N;
  cin >> N;

  int cnt = 0;
  for (int i = 0; i < N; i++) {
    int num;
    cin >> num;
    if (isPrime[num]) cnt++;
  }

  cout << cnt << '\n';
  return 0;
}

