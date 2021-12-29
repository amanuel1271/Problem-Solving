class Solution:
    def twoSum(self,nums,target):
        res = []
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                res.append([nums[i],target - nums[i]])
            seen[nums[i]] = i
                
        return res
            
        
    def threeSum(self, nums: List[int]) -> List[List[int]]: ## target  is zero
        res = []
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            for j in self.twoSum(nums[i+1:],-nums[i]):
                x = sorted([nums[i]] + j)
                if x not in res:
                    res.append(x)
            seen[nums[i]] = i
                    
        return res
            
        
