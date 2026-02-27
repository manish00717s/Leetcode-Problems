class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if k >= len(prices)//2:
            return sum(max(prices[i]-prices[i-1],0) for i in range(1,len(prices)))
        
        buy = [-10**9]*(k+1)
        sell = [0]*(k+1)

        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1]-p)
                sell[i] = max(sell[i], buy[i]+p)

        return sell[k]