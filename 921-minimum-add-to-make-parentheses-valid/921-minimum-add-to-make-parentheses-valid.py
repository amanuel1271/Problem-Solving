class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = closing = 0
        stack = deque()
        incorrect = 0
        
        for p in s:
            if p == '(':
                opening += 1
                stack.append('(')
            else:
                if stack != deque():
                    stack.pop()
                else:
                    incorrect += 1
                    
                closing += 1
          
        
        wrong = incorrect + len(stack)
        return wrong if wrong > 0 else abs(opening-closing)
        