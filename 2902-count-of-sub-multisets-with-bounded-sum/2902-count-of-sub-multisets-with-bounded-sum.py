class Solution:
    def countSubMultisets(self, nums, l, r):
        from collections import Counter
        mod = 10**9 + 7
        freq = Counter(nums)
        dp = [0]*(r+1)
        dp[0] = 1
        for val, cnt in freq.items():
            new = dp[:]
            for s in range(r+1):
                if dp[s]:
                    for k in range(1, cnt+1):
                        ns = s + k*val
                        if ns > r:
                            break
                        new[ns] = (new[ns] + dp[s]) % mod
            dp = new
        return sum(dp[l:r+1]) % mod
