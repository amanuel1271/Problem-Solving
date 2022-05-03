class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minn,maxx = math.inf,-math.inf
        is_sorted  = True
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                is_sorted = False
            if not is_sorted:
                minn = min(minn,nums[i])
                
        is_sorted = True
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                is_sorted = False
            if not is_sorted:
                maxx = max(maxx,nums[i])
        
        l,r = 0,0
        for i in range(len(nums)):
            if minn < nums[i]:
                l = i
                break
                
        for i in range(len(nums)-1,-1,-1):
            if maxx > nums[i]:
                r = i
                break
        
        
        
        return 0 if r-l+1 <= 1 else r-l+1
        
                
        
            
        
            
                
            
            
        
        
        