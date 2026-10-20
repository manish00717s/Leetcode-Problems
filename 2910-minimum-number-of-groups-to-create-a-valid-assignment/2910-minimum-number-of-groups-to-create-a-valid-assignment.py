from collections import Counter
class Solution(object):
    def minGroupsForValidAssignment(self, nums):
        freq = Counter(nums)
        min_freq = min(freq.values())
        for x in range(min_freq, 0, -1):
            total_groups = 0
            valid = True
            for f in freq.values():
                groups = f // x
                rem = f % x
                if rem > groups:
                    valid = False
                    break
                total_groups += groups
            if valid:
                return total_groups
        return len(nums)
