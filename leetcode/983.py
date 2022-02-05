class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        DAY_PASS,WEEK_PASS,MONTH_PASS = costs[0],costs[1],costs[2]
        
        @lru_cache(None)
        def dp(i,hasPass,day):
            if i == len(days):
                return 0
            
            if not hasPass:
                #have an option to buy some pass
                option1 = DAY_PASS + dp(i+1,False,0)
                option2 = WEEK_PASS + dp(i+1,True,days[i] + 7)
                option3 = MONTH_PASS + dp(i+1,True,days[i] + 30)
                return min(option1,option2,option3)
            else:
                if days[i] >= day:
                    return dp(i,False,0)
                return dp(i+1,True,day)
            
        return dp(0,False,0)
