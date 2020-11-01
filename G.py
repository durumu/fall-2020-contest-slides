n, k = map(int, input().split())
a = [int(x) for x in input().split()]

for t in range(3601):
  on = 0
  for x in a:
    if (t//x) % 2 == 1:
      on += 1
  if on >= k:
    print(t)
    exit()

print('No worries Cassie!')
