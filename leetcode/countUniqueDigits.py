
NINE = 9
class Solution:
    def __init__(self):
        self.store = {0:0,1:0,2:9}
        
    def prev_sum(self,n):
        count = 0
        for j in range(n):
            count += self.store[j] 
        return count
    
    def count_occur(self,n):
        count = NINE ## 9 digits from 1-9
        for i in range(n - 2):
            count = count * (NINE - i)  
        count = count * (n - 1)
        return count
         
        
    def find_dup(self,n):
        if n <= 1:
            return 0
        elif n == 2:
            return 9
        
        prev_dup = self.find_dup(n - 1)  
        prev_dup -= self.prev_sum(n - 1)
        self.store[n] = prev_dup * 10 + self.count_occur(n)
          
        return self.store[n] + self.prev_sum(n)
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return (10 ** n) - self.find_dup(n)
