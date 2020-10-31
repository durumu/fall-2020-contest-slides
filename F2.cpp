  int n; cin >> n;
  vector<int> A(n);

  for (int i = 0; i < n; ++i) {
    int x; cin >> x;
    for (int j = 0; j < x; ++j) {
      int b; cin >> b;
      A[i] |= 1<<(b-1); // set the bth bit
    }
  }


