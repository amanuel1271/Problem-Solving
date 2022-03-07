class Solution:
    def threeSum(self, nums,target):
        def twoSum(nums,trg):
            res = []
            seen = set()
            for i in range(len(nums)):
                if trg - nums[i] in seen:
                    res.append([nums[i],trg - nums[i]])
                seen.add(nums[i])

            return res
        
        res = []
        visited = set()
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            for j in twoSum(nums[i+1:],target-nums[i]):
                x = sorted([nums[i]] + j)
                if (x[0],x[1],x[2]) not in visited:
                    res.append(x)
                    visited.add((x[0],x[1],x[2]))
            seen.add(nums[i])
                    
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        visited  = set()
        res = []
        for i in range(len(nums)):
            for cand in self.threeSum(nums[i+1:],target-nums[i]):
                ans = sorted([nums[i]] + cand)
                tup_rep = (ans[0],ans[1],ans[2],ans[3])
                if tup_rep not in visited:
                    visited.add(tup_rep)
                    res.append(ans)
        return res
            
            
        