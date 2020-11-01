n = int(input())
a = sorted(list(map(int, input().split())))
print(a[-1] / a[0])
print(len(a), ' '.join(str(x) for x in a))
