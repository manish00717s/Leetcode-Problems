from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums):
        freq = Counter(nums)
        need = defaultdict(int)
        
        for x in nums:
            if freq[x] == 0:
                continue
            
            # Use this number
            freq[x] -= 1
            
            # Case 1: extend existing subsequence
            if need[x] > 0:
                need[x] -= 1
                need[x + 1] += 1
            
            # Case 2: start new subsequence
            elif freq[x + 1] > 0 and freq[x + 2] > 0:
                freq[x + 1] -= 1
                freq[x + 2] -= 1
                need[x + 3] += 1
            
            else:
                return False
        
        return True