n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(graph, s):

  parents = [None for _ in range(n+1)]
  parents[s] = s
  level = [[s]]

  cnt = 0
  while len(level[-1]) > 0:
    level.append([])
    for u in level[-2]:
      for v in graph[u]:
        if parents[v] is None:
          parents[v] = u
          level[-1].append(v)
          cnt += 1

  return cnt

def dfs(graph, s, parents = None, cnt = 0):

  if parents is None:
    parents = [None for _ in range(n+1)]
    parents[s] = s
    
  for v in graph[s]:
    if parents[v] is None:
      parents[v] = s
      cnt += 1
      cnt = dfs(graph, v, parents, cnt)

  return cnt

print(bfs(graph, 1))
print(dfs(graph, 1))