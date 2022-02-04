class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache(None)
        def dp(i,holding):
            ##Base case
            if i == len(prices):
                return 0
            
            do_nothing = dp(i+1,holding)
            
            if not holding:
                do_something = -prices[i] + dp(i+1,1)
            else:
                do_something = (prices[i]-fee) + dp(i+1,0)
            
            return max(do_nothing,do_something)
        
        return dp(0,0)
