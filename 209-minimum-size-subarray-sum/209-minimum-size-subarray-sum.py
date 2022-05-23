class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,window_sum = 0,0,nums[0]
        
        #initialize the window
        while r < len(nums)-1 and window_sum < target:
            r += 1
            window_sum += nums[r]
            
        if r == len(nums)-1 and window_sum < target:
            return 0
        
        
        min_len = r-l+1
        #main logic
        while l < len(nums) - 1:
            window_sum -= nums[l]
            l += 1
            while r < len(nums)-1 and window_sum < target:
                r += 1
                window_sum += nums[r]
                
            if window_sum >= target:
                min_len = min(min_len,r-l+1)
                
        return min_len
            
            
            
        
        
        
        