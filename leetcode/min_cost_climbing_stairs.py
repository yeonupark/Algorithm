def solve(cost):

  a, b = 0, 0
  for i in range(2, len(cost)):
    a, b = b, min(a + cost[i-2], b + cost[i-1]) 
  
  return min(a + cost[-2], b + cost[-1]) 