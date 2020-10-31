nxt = [None]*n
place = 0

for row in grid:
  for x in row:
    if x < n:
      nxt[x] = place
      place += 1

seen = [False]*n
repeat = 1

