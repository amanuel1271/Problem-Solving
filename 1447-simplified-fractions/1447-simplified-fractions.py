class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b%a,a)
        
        ans = []
        
        for denominator in range(2,n+1):
            for numerator in range(1,denominator):
                if numerator == 1 or gcd(numerator,denominator) == 1:
                    ans.append('{}/{}'.format(numerator,denominator))
                    
        return ans
                    
        