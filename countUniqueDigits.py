class Solution:
    def __init__(self):
        self.store = {}
        self.store[0] = 0
        self.store[1] = 0
        self.store[2] = 9
        
    def find_dup(self,n):
        if n <= 1:
            return 0
        elif n == 2:
            return 9
        
        prev_dup = self.find_dup(n - 1)
        count = 0
        
        for j in range(n - 1):
            count += self.store[j]
            
        prev_dup -= count
        
        mult_by_10 = prev_dup * 10 
        count = 9
        
        for i in range(n - 2):
            count = count * (9 - i)
            
        count = count * (n - 1)
        
        self.store[n] = mult_by_10 + count
        
        count_2 = 0
        
        for j in range(n):
            count_2 += self.store[j]
            
        return mult_by_10 + count + count_2
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return (10 ** n) - self.find_dup(n)
