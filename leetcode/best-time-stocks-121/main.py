class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        7,1,5,3,6,4
          b     s
          l       r
        """

        l = 0
        r = 0
        L = len(prices)
        max_profit = 0

        while l <= r and l < L and r < L:
            profit = prices[r] - prices[l]

            if profit < 0:
                l += 1
            else:
                r += 1
            
            max_profit = max(max_profit, profit)
        
        return max_profit




        
