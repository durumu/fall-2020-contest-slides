n, m = map(int, input().split())
rows = [input() for _ in range(n)]
cols = [''.join(tup) for tup in zip(*rows)] # transpose rows to get cols

def seq(s):
    lens = [x for x in map(len, s.split('#')) if x != 0]
    return min(lens) if lens else 10**9

ans = min(*(seq(s) for s in rows), *(seq(s) for s in cols))
print(ans)
