class Solution(object):
    def minimumSum(self, nums):
        n = len(nums)
        ans = float('inf')
        
        for j in range(1, n - 1):
            left_min = float('inf')
            right_min = float('inf')
            
            for i in range(j):
                if nums[i] < nums[j]:
                    left_min = min(left_min, nums[i])
            
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    right_min = min(right_min, nums[k])
            
            if left_min < float('inf') and right_min < float('inf'):
                ans = min(ans, left_min + nums[j] + right_min)
        
        return ans if ans != float('inf') else -1