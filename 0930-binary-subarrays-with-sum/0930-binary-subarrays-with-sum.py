from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums, goal):

        count = defaultdict(int)
        count[0] = 1

        prefix = 0
        res = 0

        for num in nums:

            prefix += num

            res += count[prefix - goal]

            count[prefix] += 1

        return res