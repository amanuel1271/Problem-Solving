class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,ptr = 1,1
        count,size = 1,len(nums)
        
        if size == 1:
            return  1
        
        
        while ptr < size:
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
                
            if count >= 3:
                nums.pop(i)
            else:
                i += 1 
            ptr += 1
            
        return i
            
        
        
        