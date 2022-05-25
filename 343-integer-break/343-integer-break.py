class Solution:
    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n):
            if n == 2:
                return 1
            elif n == 3:
                return 2
            
            maxx = 1
            for num1 in range(1,n//2 + 1):
                num2 = n - num1
                break_1 = num1 if num1 <= 3 else helper(num1)
                break_2 = num2 if num2 <= 3 else helper(num2)
                maxx = max(maxx,break_1*break_2)
            return maxx
        
        return helper(n)