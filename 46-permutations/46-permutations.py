class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(numlst):
            n = len(numlst)
            if n == 0:
                return []
            elif n == 1:
                return [[numlst[0]]]
            
            res = []
            
            for i in range(len(numlst)):
                for perms in helper(numlst[:i] + numlst[i+1:]):
                    res.append([numlst[i]] + perms)
                    
            return res
        
        return helper(nums)
                    