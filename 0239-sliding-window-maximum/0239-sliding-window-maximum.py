from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # stores indices
        result = []
        
        for i in range(len(nums)):
            # Remove elements out of window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Start adding results when window is full
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result