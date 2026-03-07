class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        dp = [1]*n
        parent = [-1]*n

        def diff(a,b):
            return sum(x!=y for x,y in zip(a,b)) == 1

        for i in range(n):
            for j in range(i):
                if groups[i]!=groups[j] and len(words[i])==len(words[j]) and diff(words[i],words[j]):
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        parent[i] = j

        idx = dp.index(max(dp))
        res = []
        while idx!=-1:
            res.append(words[idx])
            idx = parent[idx]

        return res[::-1]