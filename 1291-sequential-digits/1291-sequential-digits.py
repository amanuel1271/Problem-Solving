class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        digits = '0123456789'
        
        for digit_len in range(2,10):
            if 10**(digit_len) < low:
                continue
            elif 10**(digit_len-1) > high:
                break
                
            for starting_digit in range(1,9):
                if 9-starting_digit+1 < digit_len:
                    break
                num = int(digits[starting_digit:starting_digit+digit_len])
                if low <= num <= high:
                    ans.append(num)
                
        return ans
                    
                
            
        