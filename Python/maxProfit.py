class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price1 = 0
        price2 = 1

        while price2 < len(prices):
            if profit < (prices[price2]-prices[price1]):
                profit = prices[price2]-prices[price1]
            
            if prices[price1] > prices[price2]: 
                price1 = price2
            price2 += 1
        return profit