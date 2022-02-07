class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def my_combination(choice_list,k):
            if k == 1:
                return [[nums] for nums in choice_list]
            
            res = []
            
            for i in range(len(choice_list)):
                for combs in my_combination(choice_list[i+1:],k-1):
                    res.append([choice_list[i]] + combs)  
            return res
        
        
        n = len(nums)
        res = [[]]
        
        for k in range(1,n+1):
            for combs in my_combination(nums,k):
                res.append(combs)
        
        return res
