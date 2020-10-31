n = int(input())
a = [0] + [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

e = sorted(range(n+1), key=lambda x: d[x])

def survive(x): # try pointing at elf x
    a[0] = x
    die = [float('inf') for _ in range(n+1)]
    for elf in e:
        if die[elf] < d[elf] or a[elf] < 0:
            continue
        die[a[elf]] = min(die[a[elf]], d[elf])
    return die[0] == float('inf')

if survive(-1):
    print('fine')
else:
    for i in range(1,n+1):
        if survive(i):
            print('shoot',i)
            exit()
    print('hopeless')
