def solve(grid) -> int:
  ans = 0

  m = len(grid[0])
  n = len(grid)

  def dfs(x, y):
      dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
      
      for i in range(4):
          nx, ny = x+dx[i], y+dy[i]
          if nx >= 0 and nx < m and ny >= 0 and ny < n:
              if grid[ny][nx] == "1":
                  grid[ny][nx] = "0"
                  dfs(nx, ny)

  for i in range(len(grid)):
      for j in range(len(grid[0])):
          if grid[i][j] == "1":
              grid[i][j] = "0"
              dfs(j, i)
              ans += 1
  return ans
