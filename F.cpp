#include <bits/stdc++.h>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);

  int k; cin >> k;
  int p; cin >> p;

  int y = 0;
  for (int i = 0; i < p; ++i) {
    int b; cin >> b;
    y |= 1<<(b-1); // set the bth bit
  }
