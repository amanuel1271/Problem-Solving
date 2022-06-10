class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1,1) for i in range(len(nums))]
        max_seq_len,count = 1,0
        
        for i in range(1,len(nums)):
            max_len = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > max_len:
                        dp[i] = (dp[j][0] + 1,dp[j][1])
                    elif dp[j][0] + 1 == max_len:
                        dp[i] = (max_len,dp[i][1] + dp[j][1])
                        
                    max_len = max(max_len,dp[j][0] + 1)
                        
            max_seq_len = max(max_seq_len,max_len)
            
        #print(dp)
        return sum([cnt for num,cnt in dp if num == max_seq_len])