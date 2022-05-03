class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = 0,0
        sorted_ = sorted(nums)
        start = True
        
        for i in range(len(nums)):
            if nums[i] != sorted_[i]:
                if start:
                    l = i
                    start = False
                else:
                    r = i
                    
        return 0 if r-l+1 == 1 else r-l+1
            
                
            
            
        
        
        