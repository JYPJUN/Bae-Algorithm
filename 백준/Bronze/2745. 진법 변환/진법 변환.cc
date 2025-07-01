#include <iostream>
#include <cmath>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  string N;
  int B, result = 0;
  cin >> N >> B;
  int N_len = N.size();

  for (int i = 0; i < N_len; i++) {
    if (N[i] >= '0' && N[i] <= '9') {
      result += (N[i] - '0') * pow(B, N_len-i-1);
    } else {
      result += ((N[i]-'A') + 10) * pow(B, N_len-i-1);
    }
    
  }

  cout << result << '\n'; 

  return 0;
}
