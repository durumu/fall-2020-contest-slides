n = int(input())
a = [None] + [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

for i in sorted(range(n+1), key=lambda i: d[i]):
  if i == 0:
    break
  if a[i] != -1:
    a[a[i]] = -1

killers = [i for i in range(1, n+1) if a[i] == 0]
if a[0] == -1:
  print('hopeless')
elif len(killers) == 0:
  print('fine')
elif len(killers) == 1 and d[0] < d[killers[0]]:
  print('shoot', killers[0])
else:
  print('hopeless')
