from collections import defaultdict
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        
        ans = []
        dic = defaultdict(lambda: defaultdict(float))

        for i, eq in enumerate(equations):
            x, y = eq
            multiple = values[i]
            dic[x][y] = multiple 
            dic[y][x] = 1 / multiple

        def search(x, y, val, visited, res):
            if y in dic[x]:
                return val*dic[x][y]
            for d in dic[x]:

                if d not in visited:
                  visited.add(d)
                  res = search(d, y, val*dic[x][d], visited, res)
            return res
            
        for query in queries:
            x, y = query
            if x not in dic or y not in dic:
                ans.append(-1.0)
            else:
                ans.append(search(x, y, 1, {x}, -1))
        return ans