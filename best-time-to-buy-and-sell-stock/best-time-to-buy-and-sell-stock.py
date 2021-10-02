class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        days = len(prices)
        stocks = prices[0]
        diff = 0
        for i in range(1, days):
            if prices[i] < stocks:
                stocks = prices[i]
            else:
                diff = max(prices[i] - stocks, diff)
                print(diff)
        return diff