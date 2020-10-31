n = int(input())
beginning = input().split()
m = int(input())
ending = input().split()

for i in range(n-1, -1, -1):
    suf = beginning[i:]
    pref = ending[:min(n-i, len(ending))]
    if suf == pref:
        print(' '.join(beginning), ' '.join(ending[min(n-i, len(ending)):]))
        exit(0)

print('HOLIDAYS RUINED')