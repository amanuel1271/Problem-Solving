class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        other_colors = {0:[1,2],1:[0,2],2:[0,1]}
        
        @lru_cache(None)
        def dp(i,prev_color):
            if i == len(costs):
                return 0
            
            color1,color2 = other_colors[prev_color][0],other_colors[prev_color][1]
            
            path1 = costs[i][color1] + dp(i+1,color1)
            path2 = costs[i][color2] + dp(i+1,color2)
            
            return min(path1,path2)
        
        return min(dp(0,0),dp(0,1),dp(0,2))
            
        