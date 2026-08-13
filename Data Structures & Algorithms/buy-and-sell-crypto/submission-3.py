class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxed=0
        for i,n in enumerate(prices):
            buy = n
            sell = max(prices[i:])
            maxed = max(maxed,sell-buy)

        return maxed