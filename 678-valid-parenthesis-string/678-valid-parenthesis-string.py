class Solution:
    def checkValidString(self, s: str) -> bool:
        left_par_stack = []     # store the index of "("
        star_stack = []         # store the index of "*"
        
        for i in range(len(s)):
            if s[i] == "(":                 # When encounter "(" or "*", we store it separately as "money" for future use.
                left_par_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            elif s[i] == ")":               # When encounter ")", it's time we need to pay,
                if left_par_stack:          # we give priority to pay with "(", so the right-most "(" will be consumed.
                    left_par_stack.pop()
                elif star_stack:            # Otherwise, we pay with "*".
                    star_stack.pop()
                else:
                    return False            # We don't have enough money to pay, game over.
        
        while left_par_stack:               # In situ that some "(" haven't been consumed.
            if not star_stack:
                break
            elif star_stack[-1] > left_par_stack[-1]: # Only when the idx of "*" is greater than idx of "(" that can we apply "*" as ")"
                star_stack.pop()
                left_par_stack.pop()
            elif star_stack[-1] < left_par_stack[-1]:
                break
        
        return not left_par_stack
                    
            