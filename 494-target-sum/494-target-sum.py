class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def reach(i,total):
            if i == len(nums):
                return 1 if total == target else 0
                       
            return reach(i + 1,total + nums[i]) + reach(i + 1,total - nums[i])
        
        return reach(0,0)