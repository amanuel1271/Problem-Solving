class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0,0,0]
        
        for col in range(len(nums)):
            first,second,third = nums[col] + dp[0],nums[col] + dp[1],nums[col] + dp[2]
            dp[first%3] = max(dp[first%3],first)
            dp[second%3] = max(dp[second%3],second)
            dp[third%3] = max(dp[third%3],third)
                
        return dp[0]

        
        
        