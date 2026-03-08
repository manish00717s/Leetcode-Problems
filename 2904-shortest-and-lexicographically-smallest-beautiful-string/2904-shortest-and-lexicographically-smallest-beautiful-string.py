class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        ans = ""

        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    sub = s[i:j+1]
                    if ans == "" or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                        ans = sub
                    break

        return ans