class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxlength = 1
        
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
                    
            maxlength = max(maxlength,dp[i])
        
        return maxlength
            
        