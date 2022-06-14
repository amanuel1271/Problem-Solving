class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        l,window_product,count = 0,1,0
        for r in range(len(nums)):
            window_product *= nums[r]
            while window_product >= k:
                window_product //= nums[l]
                l += 1
                
            count += r-l+1
            
        return count
        