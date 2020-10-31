  // calculate cumulative xors
  vector<int> C(n);
  C[0] = A[0];
  for (int i = 1; i < n; ++i) C[i] = A[i] ^ C[i-1];

  int q; cin >> q;
  for (int i = 0; i < q; ++i) {
    int a, b; cin >> a >> b;
    --a; --b;
    int ans = C[b] ^ y;
    if (a) ans ^= C[a-1];
    cout << __builtin_popcount(ans) << '\n';
  }
}
