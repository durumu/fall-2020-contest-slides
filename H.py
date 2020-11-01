n = int(input())
beginning = input().split()
m = int(input())
ending = input().split()

for i in reversed(range(n)):
    suf = a[i:]
    pref = b[:min(n-i, len(b))]
    if suf == pref:
        print(' '.join(a), ' '.join(b[min(n-i, len(b)):]))
        exit()

print('HOLIDAYS RUINED')
