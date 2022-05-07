class Solution:   
    def threeSum(self, nums: List[int]) -> List[List[int]]: ## target  is zero
        
        res = []
        size = len(nums)
        nums.sort()
        
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums)-1
            target = -nums[i]
            
            if target < 2*nums[j]:
                break
            while j < k:
                if target == nums[j] + nums[k]:
                    res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    while j < k-1 and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                elif target > nums[j] + nums[k]:
                    while j < k-1 and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                else:
                    k -= 1
                    
        return res
            
            
            
            
            
            
        