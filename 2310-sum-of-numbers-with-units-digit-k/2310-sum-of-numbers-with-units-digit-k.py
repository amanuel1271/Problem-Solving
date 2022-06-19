class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        
        @lru_cache(None)
        def calculate(n):
            if n < k:
                return math.inf
            elif n == k:
                return 1
            elif n%10 == k:
                return 1
            
            minn = math.inf
            for i in range(1,n//2+1):
                n1 = calculate(i)
                n2 = math.inf
                if n1 != math.inf:
                    n2 = calculate(n-i)
                
                if n1 != math.inf and n2 != math.inf:
                    minn = min(minn,n1+n2)  
            return minn
        
        if num == 0:
            return 0
        res = calculate(num)
        return -1 if res == math.inf else res
                