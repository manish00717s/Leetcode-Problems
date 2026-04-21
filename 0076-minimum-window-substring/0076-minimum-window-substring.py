from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = {}
        
        have = 0
        need_count = len(need)
        
        left = 0
        res = [-1, -1]
        res_len = float("inf")
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                have += 1
            
            # shrink window when valid
            while have == need_count:
                # update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # remove left character
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""