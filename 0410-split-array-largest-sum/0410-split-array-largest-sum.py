class Solution:
    def splitArray(self, nums, k):
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
        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
