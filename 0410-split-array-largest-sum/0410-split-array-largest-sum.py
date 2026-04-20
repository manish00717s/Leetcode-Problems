class Solution:
    def splitArray(self, nums, k):
        
        # Helper function: can we split into ≤ k subarrays with max sum ≤ max_sum?
        def can_split(max_sum):
            count = 1
            curr = 0
            
            for num in nums:
                if curr + num > max_sum:
                    count += 1
                    curr = num
                    if count > k:
                        return False
                else:
                    curr += num
            
            return True
        
        left = max(nums)       # minimum possible answer
        right = sum(nums)      # maximum possible answer
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_split(mid):
                ans = mid
                right = mid - 1   # try smaller
            else:
                left = mid + 1    # need bigger
        
        return ans