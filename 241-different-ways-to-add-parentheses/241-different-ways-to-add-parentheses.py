class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        @lru_cache(None)
        def helper(expression):

            if ('+' not in expression) and ('-' not in expression) and ('*' not in expression):
                return [int(expression)]

            res = []

            for i, v in enumerate(expression):
                if v == '+' or v == '-' or v == '*':
                    left_res = helper(expression[:i])
                    right_res = helper(expression[i + 1:])
                    for left_v in left_res:
                        for right_v in right_res:
                            if v == '+':
                                res.append(left_v + right_v)
                            elif v == '-':
                                res.append(left_v - right_v)
                            else:
                                res.append(left_v * right_v)
            return res
        
        return helper(expression)
        
        
        
        
        
                        
                    
                    
            
            
        
        
        