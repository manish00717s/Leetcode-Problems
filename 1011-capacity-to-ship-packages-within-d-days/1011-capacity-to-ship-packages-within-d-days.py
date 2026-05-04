class Solution:
    def shipWithinDays(self, weights, days):
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            needed_days = 1
            curr_weight = 0
            
            for w in weights:
                if curr_weight + w > mid:
                    needed_days += 1
                    curr_weight = 0
                
                curr_weight += w
            
            if needed_days <= days:
                right = mid
            else:
                left = mid + 1
        
        return left