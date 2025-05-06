class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = float('inf')
        max_profit = 0

        for i in prices:
            if i < left: #if that price is less than min then that is new min
                left = i
            else:
                profit = i - left
                max_profit = max(max_profit,profit)
        
        return max_profit
        