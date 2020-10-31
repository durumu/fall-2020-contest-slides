inf = 10**9
def bfs(s):
    q = deque()
    q.appendleft(s)
    d = [inf for i in range(n)]
    d[s] = 0
    while q:
        u = q.pop()
        for v in g[u]:
            if d[v] != inf:
                continue
            d[v] = d[u]+1
            q.appendleft(v)
    return d

dist = [0]*n
for s in range(n):
    dist[s] = bfs(s)
