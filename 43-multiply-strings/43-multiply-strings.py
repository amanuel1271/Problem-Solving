class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(digit,string):
            ans,tens,num = 0,0,ord(digit) - ord('0')

            for ch in string[::-1]:
                ans += ((ord(ch) - ord('0')) * num) * (10 ** tens)
                tens += 1
                
            return ans
        
        tens = 0
        ans = 0
        
        for ch in num2[::-1]:
            ans += (mul(ch,num1)) * (10 ** tens)
            tens += 1
            
        return str(ans)
            
                
                
                
            
            
        