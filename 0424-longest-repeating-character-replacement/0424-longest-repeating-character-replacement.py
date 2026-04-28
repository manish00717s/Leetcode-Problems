from collections import defaultdict

class Solution:
    def characterReplacement(self, s, k):
        count = defaultdict(int)
        
        left = 0
        max_freq = 0
        res = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            
            # if invalid → shrink
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res