class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']   
        }
        
        self.acc = []
        
        def dfs(ans,digit):
            if digit == '':
                self.acc.append(ans)
                return
            
            for letter in digit_to_letter[digit[0]]:
                dfs(ans + letter,digit[1:])
        
        if digits == '': return []
        
        dfs('',digits)
        return self.acc
