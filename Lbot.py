from collections import defaultdict
n, k = map(int, input().split())
s = input()
nxt = [-1]*n
occ = defaultdict(lambda:-1) # dictionary with default value -1
for i in range(n):
    nxt[n-i-1] = occ[s[n-i-1]] # find most recent occurrence
    occ[s[n-i-1]] = n-i-1 # update most recent occurrence to this

dp = [[0]*(k+1) for _ in range(n)]
dp[0][0] = 1 # base case
for i in range(n-1):
    for j in range(k+1):
        if j < k and nxt[i] != -1 and nxt[i] != i+1:
            dp[nxt[i]][j+1] += dp[i][j]
        dp[i+1][j] += dp[i][j] # can always go one forward

print(sum(dp[n-1])%998244353)
