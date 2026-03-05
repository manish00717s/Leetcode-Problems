class Solution:
    def minOperations(self, s1, s2, x):
        pos = [i for i in range(len(s1)) if s1[i] != s2[i]]
        n = len(pos)
        if n % 2:
            return -1
        
        dp = [0]*(n+1)
        dp[1] = x
        
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + x, dp[i-2] + 2*(pos[i-1] - pos[i-2]))
        
        return dp[n]//2