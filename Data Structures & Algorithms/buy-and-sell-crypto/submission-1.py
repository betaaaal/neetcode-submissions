class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        maxProfit=0
        for i in range(len(prices)):
            profit=prices[i]-minPrice
            maxProfit=max(profit, maxProfit)
            minPrice=min(minPrice, prices[i])
        return maxProfit