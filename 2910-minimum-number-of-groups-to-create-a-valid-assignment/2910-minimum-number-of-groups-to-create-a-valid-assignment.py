from collections import Counter

class Solution(object):
    def minGroupsForValidAssignment(self, nums):
        freq = Counter(nums)
        
        min_freq = min(freq.values())
        
        # Try largest possible group size first
        for x in range(min_freq, 0, -1):
            total_groups = 0
            valid = True
            
            for f in freq.values():
                # number of groups if using size x
                groups = f // x
                rem = f % x
                
                # if remainder is too large, invalid
                if rem > groups:
                    valid = False
                    break
                
                total_groups += groups
            
            if valid:
                return total_groups
        
        return len(nums)  # fallback