#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int score;
  cin >> score;

  cout << (score >= 90 ? "A" : (score >=80 ? "B" : (score >= 70 ? "C" : (score >= 60 ? "D" : "F"))));

  return 0;
}