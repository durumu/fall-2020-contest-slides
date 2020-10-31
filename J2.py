# compute first spiral

grid = [[0]*side for _ in range(side)]

cur = side ** 2 - 1
for k in range(side // 2):
  grid[k][k] = cur
  for j in range(k+1, side-k):
    grid[k][j] = grid[k][j-1] - 1
  for i in range(k+1, side-k):
    grid[i][-1-k] = grid[i-1][-1-k] - 1
  for j in reversed(range(k, side-k-1)):
    grid[-1-k][j] = grid[-1-k][j+1] - 1
  for i in reversed(range(k+1, side-k-1)):
    grid[i][k] = grid[i+1][k] - 1
  cur -= 4*(side-k*2-1)


