class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        dp[(0,0)] = 1
        
        
        for i in range(len(nums)):
            for j in range(i):
                dp[(i,nums[i] - nums[j])] = dp.get((j,nums[i] - nums[j]),1) + 1
                
                
        return max(dp.values())
        
        
        
        
        