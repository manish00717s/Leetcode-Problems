class Solution:
    def maxSum(self, nums, k):
        cnt = [0]*32
        for x in nums:
            for i in range(32):
                if x >> i & 1:
                    cnt[i] += 1
        ans = 0
        mod = 10**9 + 7
        for _ in range(k):
            cur = 0
            for i in range(32):
                if cnt[i]:
                    cur |= 1 << i
                    cnt[i] -= 1
            ans = (ans + cur*cur) % mod
        return ans
