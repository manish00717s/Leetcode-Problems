class Solution:
    def deleteAndEarn(self, nums):
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for n in nums:
            points[n] += n
        take = skip = 0
        for p in points:
            take, skip = skip + p, max(skip, take)
        return max(take, skip)
