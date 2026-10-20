class Solution:
    def lastVisitedIntegers(self, words):
        nums = []
        res = []
        k = 0
        for w in words:
            if w == -1:
                k += 1
                res.append(nums[-k] if k <= len(nums) else -1)
            else:
                nums.append(w)
                k = 0
        return res
