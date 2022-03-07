class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def twoSmaller(start,thresh):
            count,left,right = 0,start,n-1
            
            while left < right:
                if (nums[left] + nums[right] < thresh):
                    count += right - left
                    left += 1
                else:
                    right -= 1
            
            return count
        
        nums.sort()
        count  = 0
        for i in range(n-2):
            count += twoSmaller(i+1,target-nums[i])
        
        return count
            
        
        