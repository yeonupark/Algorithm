def solve():
  n, m = map(int, input().split())
  r, c, d = map(int, input().split())
  rooms = []
  for _ in range(n):
    rooms.append(list(map(int, input().split())))
  
  dir = [(-1,0),(0,1),(1,0),(0,-1)]
  cnt = 0

  while True:
    if rooms[r][c] == 0:
      rooms[r][c] = -1
      cnt += 1
    cleaned = False
    
    for _ in range(len(dir)):
      d = (d-1)%4
      rn = r+dir[d][0]
      cn = c+dir[d][1]
      if rn >= 0 and rn < n and cn >= 0 and cn < m:
        if rooms[rn][cn] == 0:
          r = rn
          c = cn
          cleaned = True
          break

    if not cleaned:
      rn = r+dir[(d-2)%4][0]
      cn = c+dir[(d-2)%4][1]
      if rn < 0 or rn > n-1 or cn < 0 or cn > m-1:
        return cnt
      if rooms[rn][cn] == 1:
        return cnt
      r = rn
      c = cn

print(solve())