import sys

def solve():
  input = sys.stdin.readline

  def rotate(n, dir):
    
    if n in rotated:
      return
    
    rotated.add(n)
    tmp = points[n]
    points[n] = (points[n]-dir)%8

    if n == 1:
      if wheel[2][(points[2]+6)%8] != wheel[1][(tmp+2)%8]:
        rotate(2, dir*-1)
    elif n == 4:
      if wheel[3][(points[3]+2)%8] != wheel[4][(tmp+6)%8]:
        rotate(3, dir*-1)
    else:
      if wheel[n+1][(points[n+1]+6)%8] != wheel[n][(tmp+2)%8]:
        rotate(n+1, dir*-1)
      if wheel[n-1][(points[n-1]+2)%8] != wheel[n][(tmp+6)%8]:
        rotate(n-1, dir*-1)


  wheel = [ None for _ in range(5) ]
  for i in range(1,5):
    wheel[i] = input()
  
  points = [-1, 0, 0, 0, 0]

  k = int(input())
  for _ in range(k):
    n, dir = map(int, input().split())
    rotated = set()
    rotate(n, dir)
  
  ans = 0
  for i in range(1,5):
    if wheel[i][points[i]] == "1":
      ans += 2**(i-1)

  return ans

print(solve())
