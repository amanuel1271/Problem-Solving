class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn,best = prices[0],0
        
        for price in prices:
                minn = min(minn,price)
                best = max(best,price-minn)
        
        return best
            