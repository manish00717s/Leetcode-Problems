class Solution:
    def findIndices(self, nums, indexDifference, valueDifference):
        n = len(nums)
        min_i = max_i = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] > nums[max_i]:
                max_i = i
            if abs(nums[j] - nums[min_i]) >= valueDifference:
                return [min_i, j]
            if abs(nums[j] - nums[max_i]) >= valueDifference:
                return [max_i, j]
        return [-1, -1]
