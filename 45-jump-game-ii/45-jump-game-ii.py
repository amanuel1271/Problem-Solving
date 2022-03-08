class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        
        dp[-1] = 0 # base case
        
        for j in range(n-2,-1,-1):
            if nums[j] == 0:
                continue
                
            min_ = math.inf
            for i in range(1,nums[j] + 1):
                if j+i < n:
                    min_ = min(min_,dp[j+i] + 1)
                    
            dp[j] = min_
            
            
        return dp[0]
        