class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        
        back,front = 0,0
        for i in range(len(nums)):
            cur = nums[i] * count[nums[i]]
            
            if i > 0 and nums[i] == nums[i-1] + 1:
                back,front = front,max(cur + back,front)
            else:
                back,front = front,front + cur
                
        return front
                
            
        