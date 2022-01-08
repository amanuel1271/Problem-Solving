class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
	    # helper
        dp = {}
        
        def reach(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (total,i) in dp:
                return dp[(total,i)]
            
            dp[(total,i)] = reach(i + 1,total + nums[i]) + reach(i + 1,total - nums[i])
            
            return dp[(total,i)]
        
        return reach(0,0)
