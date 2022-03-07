class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        def backtrack(i=0, solution=[]):
            if len(solution) == k:
                ans.append(solution[:])
                return
            
            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j-1]:
                    continue
                solution.append(nums[j])
                backtrack(j+1, solution)
                solution.pop()
                
        for k in range(n+1):
            backtrack()
        return ans
                
        