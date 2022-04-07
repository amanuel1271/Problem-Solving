class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        sum_ = 0
        
        for i,a in enumerate(nums):
            sum_ += a
            if sum_ % k in d and i - d[sum_ % k] >= 2:
                return True
            
            if sum_ % k not in d: 
                d[sum_ % k] = i
                
        return False
        