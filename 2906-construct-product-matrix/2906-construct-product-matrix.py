class Solution:
    def constructProductMatrix(self, grid):
        mod = 12345
        m, n = len(grid), len(grid[0])
        
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = m * n
        left = [1]*size
        right = [1]*size
        
        for i in range(1, size):
            left[i] = (left[i-1] * arr[i-1]) % mod
        
        for i in range(size-2, -1, -1):
            right[i] = (right[i+1] * arr[i+1]) % mod
        
        res = []
        for i in range(size):
            res.append((left[i] * right[i]) % mod)
        
        # reshape back to matrix
        ans = []
        idx = 0
        for i in range(m):
            ans.append(res[idx:idx+n])
            idx += n
        
        return ans