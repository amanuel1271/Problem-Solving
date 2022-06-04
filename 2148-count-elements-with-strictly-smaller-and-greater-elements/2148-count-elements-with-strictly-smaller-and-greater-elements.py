class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        left,right = nums[0],nums[-1]
        
        for num in nums:
            if left < num < right:
                count += 1
                
        return count
        
        