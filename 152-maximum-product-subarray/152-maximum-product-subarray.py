class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        curmin,curmax = 1,1
        
        
        
        for n in nums:
            tmp = curmax * n
            curmax = max(curmax * n,n * curmin,n)
            curmin = min(tmp,n * curmin,n)
            res = max(res,curmax)
            
        return res
        
        