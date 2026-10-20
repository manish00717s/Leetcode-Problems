class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = {}
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            ans = 1
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    matrix[nr][nc] > matrix[r][c]):
                    ans = max(ans, 1 + dfs(nr, nc))
            dp[(r, c)] = ans
            return ans
        return max(dfs(i, j) for i in range(m) for j in range(n))
