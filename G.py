n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

ans = 0
for i in range(n-k+1):
    if a[i:i+k] == b:
        a[i+k-1] = 0
        ans += 1

print(ans)