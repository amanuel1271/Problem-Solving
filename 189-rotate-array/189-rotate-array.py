class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,j):
            while i < j:
                nums[j],nums[i] = nums[i],nums[j]
                i += 1
                j -= 1
                
        n = len(nums)
        k %= n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n- 1)
        
        
        
        
    
            
                
            
        
        