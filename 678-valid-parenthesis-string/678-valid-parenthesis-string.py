class Solution:
    def checkValidString(self, s: str) -> bool:
        left_par_stack = deque()     
        star_stack = deque()        
        
        for i in range(len(s)):
            if s[i] == "(":                 
                left_par_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            elif s[i] == ")":               
                if left_par_stack:          
                    left_par_stack.pop()
                elif star_stack:           
                    star_stack.pop()
                else:
                    return False            
        
        while left_par_stack:  
            if not star_stack:
                break
            elif star_stack[-1] > left_par_stack[-1]:
                star_stack.pop()
                left_par_stack.pop()
            elif star_stack[-1] < left_par_stack[-1]:
                break
        
        return not left_par_stack
                    
            