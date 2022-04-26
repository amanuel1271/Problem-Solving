class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        overall_score = sum(nums)
        size = len(nums)

        
        #@lru_cache(None)
        def dfs(i,j,p1_score,turn_1):
            if j < i:
                return p1_score >= overall_score - p1_score
            
            move_1,move_2 = False,False
            if turn_1:
                return dfs(i+1,j,p1_score + nums[i],0) or dfs(i,j-1,p1_score + nums[j],0)
            else:
                return dfs(i+1,j,p1_score,1) and dfs(i,j-1,p1_score,1)
                
        

        return dfs(0,size-1,0,1)
                
                
            
            
        