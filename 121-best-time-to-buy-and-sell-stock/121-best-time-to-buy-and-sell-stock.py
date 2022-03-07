class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curbest,best = prices[0],0
        
        for price in prices:
            if price <= curbest:
                curbest = price
            else:
                best = max(best,price-curbest)
        
        return best
            