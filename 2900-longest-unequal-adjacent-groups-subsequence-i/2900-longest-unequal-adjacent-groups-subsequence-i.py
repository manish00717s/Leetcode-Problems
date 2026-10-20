class Solution:
    def getLongestSubsequence(self, words, groups):
        res = [words[0]]
        last = groups[0]
        for i in range(1, len(words)):
            if groups[i] != last:
                res.append(words[i])
                last = groups[i]
        return res
