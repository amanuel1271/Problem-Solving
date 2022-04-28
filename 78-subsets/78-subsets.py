class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        
        hold = []
        def backtrack(i):
            if i == len(nums):
                res.append(hold[:])
                return
                
            hold.append(nums[i])
            backtrack(i+1)
            
            hold.pop()
            backtrack(i+1)
            
        
        backtrack(0)
        return res
                
            
    
            
        
        
        