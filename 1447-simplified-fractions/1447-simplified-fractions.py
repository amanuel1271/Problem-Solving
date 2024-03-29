class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            while a:
                a,b = b%a,a 
            return b
        
        ans = []
        
        for denominator in range(2,n+1):
            for numerator in range(1,denominator):
                if gcd(numerator,denominator) == 1:
                    ans.append('{}/{}'.format(numerator,denominator))
                    
        return ans
                    
        