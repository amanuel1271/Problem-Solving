class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i,holding,sold_day_before):
            # Base case
            if i == len(prices): 
                return 0
            
            do_nothing = dp(i + 1, holding,sold_day_before)
            do_something = 0

            if not holding and not sold_day_before:
                do_something = -prices[i] + dp(i + 1,1,0)
            elif not holding and sold_day_before:
                do_something = dp(i + 1,0,0)
            else:
                do_something = prices[i] + dp(i + 1,0,1)

            # Recurrence relation
            return max(do_nothing, do_something)

        return dp(0,0,0)
