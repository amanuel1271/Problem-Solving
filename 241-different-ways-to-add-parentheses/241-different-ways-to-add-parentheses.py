class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        operation_dict = {'+':lambda x,y: x + y,'-':lambda x,y: x - y,'*':lambda x,y: x * y}
        
        @lru_cache(None)
        def helper(expression):

            if ('+' not in expression) and ('-' not in expression) and ('*' not in expression):
                return [int(expression)]

            res = []
            for i, v in enumerate(expression):
                if v in operation_dict:
                    left_res = helper(expression[:i])
                    right_res = helper(expression[i + 1:])
                    for left_v in left_res:
                        for right_v in right_res:
                            res.append(operation_dict[v](left_v,right_v))
            return res
        
        return helper(expression)
        
        
        
        
        
                        
                    
                    
            
            
        
        
        