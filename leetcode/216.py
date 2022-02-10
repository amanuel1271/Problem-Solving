class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(choice_list,k):
            if k == 1:
                return [[nums] for nums in choice_list]
            
            res = []
            
            for i in range(len(choice_list)):
                the_rest = choice_list[i+1:]
                
                for combs in backtrack(the_rest,k-1):
                    res_lst = [choice_list[i]] + combs
                    if sum(res_lst) > n:
                        continue
                    res.append(res_lst)
                
            return res
        
        choice_list = [i for i in range(1,10)]
        for cand in backtrack(choice_list,k):
            if sum(cand) == n:
                res.append(cand)
        return res
