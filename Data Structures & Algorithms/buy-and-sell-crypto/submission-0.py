class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_buying_price=float('inf')
        for price in prices:
            if price<min_buying_price:
                min_buying_price=price
            if price-min_buying_price>=0:
                profit=price-min_buying_price
                max_profit=max(profit,max_profit)
        return max_profit