class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxed=0
        left = 0
        for right in range(1,len(prices)):
            if prices[left] > prices[right]: # if buy day is more expensive than sell day,
                left = right
            else: #profit can be made cause buy day less than sell day
                profit = prices[right] - prices[left]
                maxed = max(maxed, profit)

        return maxed