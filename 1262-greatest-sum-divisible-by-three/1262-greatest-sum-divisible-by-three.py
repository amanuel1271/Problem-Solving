class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(3)]
        # for i in range(3):
        #     z = []
        #     for j in range(len(nums)):
        #         z.append(0)
        #     dp.append(z)
            
        print(dp)
        dp[nums[0]%3][0] = nums[0]
        for i in range(1,len(nums)):
            for j in range(3):
                x = dp[j][i-1] + nums[i]
                dp[x%3][i] = max([dp[x%3][i], x, dp[x%3][i-1]])
                dp[j][i] = max(dp[j][i-1],dp[j][i])
        return dp[0][-1]

        
        
        