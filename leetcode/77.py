class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(choice_list,k):
            if k == 1:
                return [[nums] for nums in choice_list]
            
            res = []
            
            for i in range(len(choice_list)):
                for combs in helper(choice_list[i+1:],k-1):
                    res.append([choice_list[i]] + combs)
                
            return res
        
        choice_list = [i for i in range(1,n+1)]
        return helper(choice_list,k)
