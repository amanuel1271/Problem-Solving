class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        
        @lru_cache(None)
        def dp(i,prev_color):
            if i == len(costs):
                return 0
            
            minpath = math.inf
            for color in range(k):
                if color != prev_color:
                    minpath = min(minpath,costs[i][color] + dp(i+1,color))
            
            return minpath
        
        minn = math.inf
        for i in range(k):
            minn = min(minn,dp(0,i))
        
        return minn
        