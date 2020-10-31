q = int(input())
for i in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    d = dist[u][v]
    if d >= inf:
        d = -1
    print(d)
