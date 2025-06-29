#include <iostream>
#include <iomanip>
#include <map>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  double total_score = 0;
  double total_credit = 0;

  map<string, double> grade_map = {
    {"A+", 4.5}, {"A0", 4.0}, 
    {"B+", 3.5}, {"B0", 3.0}, 
    {"C+", 2.5}, {"C0", 2.0}, 
    {"D+", 1.5}, {"D0", 1.0}, 
    {"F", 0.0}, 
  };

  for (int i = 0; i< 20; i++) {
    string subject, grade;
    double credit;
    cin >> subject >> credit >> grade;
    
    if (grade == "P") continue;

    total_credit += credit;
    total_score += credit * grade_map[grade];
    
  }

  cout << fixed << setprecision(9) << total_score / total_credit << '\n';

  return 0;
}