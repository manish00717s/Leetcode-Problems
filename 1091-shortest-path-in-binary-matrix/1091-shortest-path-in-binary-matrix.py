from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        dirs = [(1,0),(-1,0),(0,1),(0,-1),
                (1,1),(1,-1),(-1,1),(-1,-1)]
        while q:
            r, c, d = q.popleft()
            if r == n-1 and c == n-1:
                return d
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and
                    grid[nr][nc] == 0):
                    grid[nr][nc] = 1
                    q.append((nr, nc, d + 1))
        return -1
