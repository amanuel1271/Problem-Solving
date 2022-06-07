class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        MAX_INTEGER = 2**31-1
        
        digits = list(str(n))
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
            
        if i == 0: return -1
        
        j = len(digits)-1
        while j > i-1 and digits[j] <= digits[i-1]:
            j -= 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        res = int(''.join(digits))
        
        return res if res <= MAX_INTEGER else -1
    
        