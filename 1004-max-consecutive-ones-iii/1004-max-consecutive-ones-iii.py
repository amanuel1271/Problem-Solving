class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount,res,start = 0,0,0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeroCount += 1
            if zeroCount > k:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
                
            res= max(res,end-start+1)
                
        return res
        