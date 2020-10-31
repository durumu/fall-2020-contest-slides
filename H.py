n = int(input())
a = input().split()
m = int(input())
b = input().split()

for i in range(n-1, -1, -1):
    suf = a[i:]
    pref = b[:min(n-i, len(b))]
    if suf == pref:
        print(' '.join(a), ' '.join(b[min(n-i, len(b)):]))
        exit(0)

print('HOLIDAYS RUINED')