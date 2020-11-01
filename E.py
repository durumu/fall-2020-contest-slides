import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
p = []
for i in range(n):
    p.append((a[i] - c[i]) / b[i])
p = sorted(p)
for i in range(q):
    k = int(input())
    i = bisect.bisect(p, k)
    print(i)
