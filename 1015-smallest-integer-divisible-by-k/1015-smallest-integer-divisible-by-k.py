class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Numbers ending with 0,2,4,5,6,8 can never divide a repunit
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            
            if remainder == 0:
                return length
        
        return -1