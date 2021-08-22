class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==  1:
            return nums[0]
        
        len_  = len(nums) - 1
        dic = {}
        dic[len_] = nums[-1]
        
        for i in range(len_):
            reversed_i = len_ - i - 1
            dic[reversed_i] = max(dic[reversed_i + 1] + nums[reversed_i],nums[reversed_i])
            
        max_ = dic[len_]
        for val in dic.values():
            if val > max_:
                max_ = val
            
        return max_
