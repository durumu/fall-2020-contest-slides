dp = [[-1]*(k+1) for _ in range(n)]
# define f
def f(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    if i == 0:
        dp[i][j] = j == 0
    elif prev[i] == -1 or prev[i] == i-1 or j == 0:
        dp[i][j] = f(i-1, j)
    else:
        dp[i][j] = f(i-1, j) + f(prev[i], j-1)

    return dp[i][j]

print(sum(f(n-1, i) for i in range(k+1))%998244353)
