class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index,index2 = 0,len(nums)-1
        i = 0
        
        while i <= index2:
            if nums[i] == 0:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
            elif nums[i] == 2:
                nums[i],nums[index2] = nums[index2],nums[i]
                index2 -= 1
                continue
                
            i += 1
        