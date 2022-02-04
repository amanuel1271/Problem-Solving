class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        other_colors = {0:[1,2],1:[0,2],2:[0,1]}
        
        @lru_cache(None)
        def dp(i,prev_color):
            if i == len(costs):
                return 0
            
            color_1,color_2 = other_colors[prev_color][0],other_colors[prev_color][1]
            
            path_1 = costs[i][color_1] + dp(i+1,color_1)
            path_2 = costs[i][color_2] + dp(i+1,color_2)
            
            return min(path_1,path_2)
        
        return min(dp(0,0),dp(0,1),dp(0,2))
