class Solution:
    def isValid(self, s: str) -> bool:
        brac_dic = {'}':'{',')':'(',']':'['}
        stack = deque()
        
        for par in s:
            if par not in brac_dic:
                stack.append(par)
            else:
                opening = brac_dic[par]
                if stack == deque() or (stack.pop() != opening):
                    return False
                
        return stack == deque()
                
            
            
        
        