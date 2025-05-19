class Solution:
    
    def search_edge(self, board, exclude, x, y):
        
        exclude.add((y, x))
        levels = [(y, x)]
        dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)

        while len(levels) > 0:
          cy, cx = levels.pop()

          for dir in range(4):
              ny = cy + dy[dir]
              nx = cx + dx[dir]
              if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                  if board[ny][nx] == 'O' and (ny, nx) not in exclude:
                      exclude.add((ny, nx))
                      levels.append((ny, nx))
        return exclude
    
    def solve(self, board):
        m = len(board)
        n = len(board[0])

        exclude = set()

        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in exclude:
                    exclude = self.search_edge(board, exclude, j, i)
        for i in range(1, m-1):
            for j in [0, n-1]:
                if board[i][j] == 'O' and (i,j) not in exclude:
                    exclude = self.search_edge(board, exclude, j, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in exclude:
                    board[i][j] = 'X'
