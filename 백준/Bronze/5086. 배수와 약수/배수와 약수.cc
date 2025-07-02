#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int a, b;

  while (true) {
    int flag = 0;
    cin >> a >> b;
    if (a==0 && b ==0) break;

    if (b % a == 0) flag = 1;
    if (a % b == 0) flag = 2;
    
    if (flag) {
      if (flag == 1) cout << "factor" << '\n';
      else cout << "multiple" << '\n';
    } 
    else cout << "neither" << '\n';

  }

  return 0;
}