from collections import defaultdict

n, k = map(int, input().split())
s = input()

# precalculate prev[i]
prev = [-1]*n
occ = defaultdict(lambda:-1) # dictionary with default value -1
for i in range(n):
    prev[i] = occ[s[i]] # find most recent occurrence
    occ[s[i]] = i # update most recent occurrence to this one


