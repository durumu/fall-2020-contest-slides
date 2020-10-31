from math import ceil, gcd

def lcm(x, y):
  return x // gcd(x, y) * y

n = int(input())
side = ceil(n**0.5)
if side % 2 == 1:
  side += 1


