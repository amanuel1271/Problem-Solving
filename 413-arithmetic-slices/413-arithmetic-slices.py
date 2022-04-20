class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        count = 0
        i = 0
        
        while i < size - 2:
            j = i + 1
            diff = nums[j] - nums[i]
            
            while j < size:
                if nums[j] - nums[j-1] == diff:
                    j += 1
                else:
                    break
                    
            if j - i >= 3:
                count += ((j - i - 2)*(j - i - 1)//2)   
                
            i = j - 1
        
        return count
                    
            
            