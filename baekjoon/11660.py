import sys

def solve():
  input = sys.stdin.readline
  n, m = map(int, input().split())
  ch = [ None for _ in range(n) ]
  for i in range(n):
    ch[i] = tuple(map(int, input().split()))
  
  targets = [None for _ in range(m)]
  for i in range(m):
    targets[i] = tuple(map(int, input().split()))
  
  dp = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if j == 0:
        dp[i][j] = ch[i][j]
      dp[i][j] = dp[i][j-1] + ch[i][j]
  
  for (x1, y1, x2, y2) in targets:
    ans = 0
    for x in range(x1, x2+1):
      if y1 == 1:
        ans += dp[x-1][y2-1]
      else:
        ans += dp[x-1][y2-1] - dp[x-1][y1-2]
    print(ans)

solve()