class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        DAY_PASS,WEEK_PASS,MONTH_PASS = costs[0],costs[1],costs[2]
        
        @lru_cache(None)
        def dp(i,day):
            if i == len(days):
                return 0
            
            if day == -1: # means no pass, so needs a new one
                option1 = DAY_PASS + dp(i+1,-1)
                option2 = WEEK_PASS + dp(i+1,days[i] + 7)
                option3 = MONTH_PASS + dp(i+1,days[i] + 30)
                return min(option1,option2,option3)
            else:
                if days[i] >= day:
                    return dp(i,-1)
                return dp(i+1,day)
            
        return dp(0,-1)
