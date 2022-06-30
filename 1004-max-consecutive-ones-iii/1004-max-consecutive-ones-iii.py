class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount,res,l = 0,0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            if zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
                
            res= max(res,r-l+1)
                
        return res
        