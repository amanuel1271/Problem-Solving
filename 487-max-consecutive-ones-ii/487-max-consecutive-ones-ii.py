class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr,prev,seenZero = 0,0,0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                seenZero = 1
                prev = curr
                curr = 0
            else:
                curr += 1
            
            maxx = max(maxx,curr + prev + seenZero)
        return maxx
                
            
        