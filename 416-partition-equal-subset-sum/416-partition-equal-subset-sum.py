class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target  = total_sum//2
        
        @lru_cache(None)
        def dfs(i,trg):
            if trg == 0:
                return True
            if i >= size:
                return False
            
            return dfs(i+1,trg - nums[i]) or dfs(i+1,trg)
            
            
        return dfs(0,target)
            
            
        
        
        