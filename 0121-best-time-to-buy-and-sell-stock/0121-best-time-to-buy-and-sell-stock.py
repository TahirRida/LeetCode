class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for i in range(len(prices)):
            max_profit = max(max_profit,prices[i]-prices[left])
            left = i if prices[i]<prices[left] else left
        return max_profit