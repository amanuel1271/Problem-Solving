class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr,ans):
            if len(arr) == 0:
                res.append(ans[:])

            for num in arr:
                ans.append(num)
                backtrack(arr - {num},ans)
                ans.remove(num)
        
        
        backtrack(set(nums),[])
        return res
                    