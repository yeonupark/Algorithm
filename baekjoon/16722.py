import sys

def solve():
  input = sys.stdin.readline

  cards = [None] * 10 
  for i in range(1,10):
    cards[i] = tuple(input().rstrip().split())

  match = {-1}
  for i in range(1,8):
    for j in range(i+1,9):
      for k in range(j+1,10):

        isMatch = True
        for p in range(3):
          if len({cards[i][p][0], cards[j][p][0], cards[k][p][0]}) == 2:
            isMatch = False
            break
        if isMatch:
          match.add(f"{i}{j}{k}")
          
  score = 0
  n = int(input())
  for _ in range(n):
    ans = input()
    if ans[0] == "H":
      a, b, c = sorted(ans.split()[1:])
      if a+b+c in match:
        match.remove(a+b+c)
        score += 1
      else:
        score -= 1
    else:
      if match == {-1}:
        match.remove(-1)
        score += 3
      else:
        score -= 1
  return score

print(solve())