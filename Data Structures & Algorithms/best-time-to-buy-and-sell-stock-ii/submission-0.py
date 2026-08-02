class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all_profits=0
        left=0
        right=1
        while right<len(prices):
            if prices[right]<prices[left]:
                left=right
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                all_profits+=profit
                left=right
            right+=1
        return all_profits