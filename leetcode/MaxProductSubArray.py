class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) ==  1:
            return nums[0]
        
        len_  = len(nums) - 1
        dic = {}
        dic_min = {}
        dic[len_] = nums[-1]
        dic_min[len_] = nums[-1]
        
        for i in range(len_):
            reversed_i = len_ - i - 1
            if nums[reversed_i] >= 0:
                dic[reversed_i] = max(dic[reversed_i + 1] * nums[reversed_i],nums[reversed_i])
                dic_min[reversed_i] = min(dic_min[reversed_i + 1] * nums[reversed_i],nums[reversed_i])
            else:
                dic[reversed_i] = max(dic_min[reversed_i + 1] * nums[reversed_i],nums[reversed_i])
                dic_min[reversed_i] = min(dic_min[reversed_i + 1] * nums[reversed_i],nums[reversed_i],dic[reversed_i + 1] * nums[reversed_i])
                   
        return max(dic.values()):
           
    
        
