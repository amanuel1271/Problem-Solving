class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        reset = True
        count = 0
        max_ = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                reset = True
                max_ = max(max_,count)
                count = 0
            else:
                if reset:
                    count = 1
                else:
                    count += 1
                reset = False
                
                
        return max(max_,count)
        