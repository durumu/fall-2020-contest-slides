from math import factorial
from collections import Counter
input() # ignore n
counts = Counter(map(int, input().split()))

ways = 1
for count in counts.values():
    ways *= factorial(count)
    ways %= 998244353
print(ways)