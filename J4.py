# get lcm of cycle lengths

for i in range(n):
  cur = i
  cycle_length = 0
  while not seen[cur]:
    seen[cur] = True
    cur = nxt[cur]
    cycle_length += 1
  if cycle_length > 1:
    repeat = lcm(repeat, cycle_length)
  if repeat > 10**18:
    break

if repeat > 10**18:
  print('SING FOREVER')
else:
  print(repeat)
