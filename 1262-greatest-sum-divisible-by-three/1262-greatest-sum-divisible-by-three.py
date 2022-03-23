class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        row_size,col_size = 3,len(nums)
        dp = [[0 for _ in range(col_size)] for _ in range(row_size)]
        dp[nums[0]%3][0] = nums[0]
        
        
        for i in range(1,col_size):
            for j in range(3):
                dp[j][i] = max(dp[j][i-1],dp[j][i])
                x = dp[j][i-1] + nums[i]
                dp[x%3][i] = max([dp[x%3][i], x, dp[x%3][i-1]])
                
        return dp[0][-1]

        
        
        