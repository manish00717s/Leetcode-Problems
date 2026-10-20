class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k if k != 0 else curr_sum
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        return False
