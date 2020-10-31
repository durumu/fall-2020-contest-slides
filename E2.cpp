  vector<double> ans(n+2); // stores probability for each place
  // loop through all bitmasks of length n
  for (int msk = 0; msk < (1<<n); ++msk) {
    double pr = 1; // probability of event
    int place = 1; // place it gets us

    for (int i = 0; i < n; ++i) { // calculate event probability
      if (msk&(1<<i)) {
        pr *= p[i];
        if (s[i] > k) ++place;
      } else {
        pr *= (1-p[i]);
      }
    }

    ans[place] += pr; // add this event probability to the place it gets us
  }

  for (int i = 1; i <= n+1; ++i) cout << fixed << setprecision(8) << ans[i] << ' ';
  cout << '\n';
}
