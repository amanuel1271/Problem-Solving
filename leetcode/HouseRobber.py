class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        if len(nums) == 1:
            return dp[-1]
        
        dp[1] = max(nums[0],nums[1])
        
        for j in range(2,len(nums)):
            dp[j] = max(nums[j] + dp[j - 2],dp[j-1])
            
        return dp[-1]
