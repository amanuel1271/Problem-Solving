class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]
        max_ = prices[-1]
        for i in range(len(prices) - 1):
            if max_ - prices[-2-i] > dp[-1]:
                dp.append(max_ - prices[-2-i])
            max_ = max(max_,prices[-2-i])
            
        return dp[-1]
