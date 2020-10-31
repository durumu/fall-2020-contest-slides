def unshuffle(a):
    return a[0::2] + a[1::2]

n = int(input())

a = list(range(n))
b = unshuffle(a)
ct = 1
while a != b:
    b = unshuffle(b)
    ct += 1

print(ct)