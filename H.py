from collections import deque

n, m = map(int, input().split())
g = [ [] for _ in range(n) ]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

