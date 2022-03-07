class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            
            root = helper(x,n//2) 
            
            if n % 2 == 0: 
                return root * root
            else:
                return root * (x * root)
            
        if n >= 0:
            return helper(x,n)
        else:
            return 1 / helper(x,-n)
        