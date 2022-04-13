class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        zeroes = s.count('0')
        ans = zeroes
        
        
            
        for j in range(len(s)):
            if s[j] == '0':
                zeroes -= 1
            else:
                ones += 1
                
            ans = min(ans,ones + zeroes)
                
    
        return ans
                
            
        