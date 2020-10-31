#include <bits/stdc++.h>

using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);

  int n, m;
  cin >> n >> m;

  vector<string> rows(n), cols(m);
  for (int i = 0; i < n; ++i) cin >> rows[i];
  for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
    cols[j].push_back(rows[i][j]);
  }

  auto seq = [&](string &s) {
    int cnt = 0, ans = 1e9;
    for (int i = 0; i < int(s.size()); ++i) {
      if (s[i] == '.') {
        ++cnt;
      } else {
        if (cnt) ans = min(ans, cnt);
        cnt = 0;
      }
    }
    if (cnt) ans = min(ans, cnt);
    return ans;
  };

  int ans = 1e9;
  for (auto s: rows) ans = min(ans, seq(s));
  for (auto s: cols) ans = min(ans, seq(s));
  cout << ans << '\n';
}
