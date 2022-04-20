class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        size = len(nums)
        dp = [[nums[i]] for i in range(size)]
        
        
        for i in range(1,size):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]

        
        max_index,max_size = 0,1
        for i in range(1,size):
            size_i = len(dp[i])
            if size_i > max_size:
                max_size = size_i
                max_index = i
                
        return dp[max_index]
        
        