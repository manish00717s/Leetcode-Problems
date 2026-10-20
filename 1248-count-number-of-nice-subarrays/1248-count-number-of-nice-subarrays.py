from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums, k):
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        res = 0
        for num in nums:
            prefix += num % 2
            res += count[prefix - k]
            count[prefix] += 1
        return res
