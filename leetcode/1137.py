class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
            
        
        back_back,back,front = 0,1,1
        
        for j in range(3,n + 1):
            back_back,back,front = back,front,front + back_back + back
        
        return front
