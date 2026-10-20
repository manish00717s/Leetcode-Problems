from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        maxD = deque()
        minD = deque()
        left = 0
        res = 0
        for right in range(len(nums)):
            while maxD and nums[right] > maxD[-1]:
                maxD.pop()
            while minD and nums[right] < minD[-1]:
                minD.pop()
            maxD.append(nums[right])
            minD.append(nums[right])
            while maxD[0] - minD[0] > limit:
                if nums[left] == maxD[0]:
                    maxD.popleft()
                if nums[left] == minD[0]:
                    minD.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res
