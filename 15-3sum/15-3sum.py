class Solution:   
    def threeSum(self, nums: List[int]) -> List[List[int]]: ## target  is zero
        def twoSum(nums,target):
            res = []
            seen = set()
            for i in range(len(nums)):
                if target - nums[i] in seen:
                    res.append([nums[i],target - nums[i]])
                seen.add(nums[i])

            return res
        
        res = []
        visited = set()
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            for j in twoSum(nums[i+1:],-nums[i]):
                x = sorted([nums[i]] + j)
                if (x[0],x[1],x[2]) not in visited:
                    res.append(x)
                    visited.add((x[0],x[1],x[2]))
            seen.add(nums[i])
                    
        return res
            
        