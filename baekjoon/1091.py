import sys

def solve():
  input = sys.stdin.readline

  n = int(input())
  cards = [ i for i in range(n) ]
  p = tuple(map(int, input().split()))
  s = tuple(map(int, input().split()))

  done = True
  target = {0: set(), 1: set(), 2: set()}
  for i in range(n):
    target[p[i]].add(cards[i])

    if done:
      if cards[i] == 0:
        if p[i] != 0:
          done = False
      elif cards[i]%3 != p[i]:
        done = False

  if done:
    return 0
  
  cnt = 0
  first_cards = cards
  while True:
    cnt += 1
    copylist = [ elem for elem in cards ]
    copy = {0: set(), 1: set(), 2: set()}
    for i in range(n):
      copylist[s[i]] = cards[i]
      copy[s[i]%3].add(cards[i])
    cards = copylist

    if copy == target:
      return cnt
    
    if cards == first_cards:
      return -1

print(solve())
