#include <iostream>
using namespace std;

int main() {
  int n; cin >> n;

  int shuffles = 1, x = 2 % (n-1);
  while (x != 1 % (n-1)) {
    x = 2*x % (n-1);
    ++shuffles;
  cout << shuffles << endl;
}