class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        curmin,curmax = 1,1
        
        
        
        for n in nums:
            curmax,curmin = max(curmax*n,curmin*n,n),min(curmax * n,curmin * n,n)
            res = max(res,curmax)
            
        return res
        
        