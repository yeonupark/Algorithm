n, k = map(int, input().split())
belt = list(map(int, input().split()))
robots = [False for _ in range(n)]

def solve(belt, robots, k, level):
  if k <= 0:
    return level
  
  level += 1
  belt = [belt[-1]]+belt[0:2*n-1]
  robots = [False]+robots[0:n-1]
  robots[-1] = False
  
  for i in range(n-1,-1,-1):
    if robots[i]:
      next = (i+1)%(2*n)
    
      if belt[next] > 0:
        if i == n-1:
          robots[i] = False
          belt[next] -= 1
        elif not robots[i+1]:
          robots[i] = False
          robots[i+1] = True
          belt[next] -= 1

        if belt[next] == 0:
          k -= 1

  if belt[0] != 0:
    robots[0] = True
    belt[0] -= 1

    if belt[0] == 0:
      k -= 1
  return solve(belt, robots, k, level)

print(solve(belt, robots, k, 0))
