n = int(input())
a = list(map(int, input().split()))
a = sorted((a[i], i) for i in range(n))
l = list(map(int, input().split()))
l = sorted((l[i], i) for i in range(n))
ans = [0]*n
for i in range(n):
    x, j = a[i]
    y, k = l[i]
    if y < x:
        print('NO')
        exit()
    ans[k] = j+1
print('YES')
print(' '.join(str(x) for x in ans))
