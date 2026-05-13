class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxProfit=0
        for i in range(n):
            for j in range(i+1,n):
                profit=prices[j]-prices[i]
                maxProfit=max(profit,maxProfit)
        return maxProfit