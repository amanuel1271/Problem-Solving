class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'   
        }
        
        self.acc = []
        
        def helper(ans,digit):
            if digit == '':
                self.acc.append(ans)
                return
            
            for letter in digit_to_letter[digit[0]]:
                helper(ans + letter,digit[1:])
        
        if digits == '': return []
        
        helper('',digits)
        return self.acc
                
        