def solve():
  
  def roll(dir):
    if dir == 1:
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif dir == 2:
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] 
    elif dir == 3:
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] 
    else:
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4] 

  n, m, x, y, _ = map(int, input().split())
  dice = [0 for i in range(1,7)]

  board = [ None for _ in range(n) ]
  for i in range(n):
    board[i] = list(map(int, input().split()))
  orders = map(int, input().split())

  cx, cy = x, y
  dx, dy = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)

  answer = []
  for o in orders:
    nx, ny = cx + dx[o], cy + dy[o]
    if nx >= 0 and ny >= 0 and nx < n and ny < m:

      cx, cy = nx, ny
      roll(o)

      answer.append(str(dice[0]))
      if board[cx][cy] != 0:
        dice[5] = board[cx][cy]
        board[cx][cy] = 0
      else:
        board[cx][cy] = dice[5]

  print("\n".join(answer))

solve()