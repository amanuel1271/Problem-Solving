class Solution:
    def __init__(self):
        self.dp = {}
        self.dp[1] = 1
        self.dp[2] = 2    
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        count = 0
        x = {}
        
        for num in range(1,n+1):
            if num == 1 or num == n:
                if n-1 in self.dp:
                    count += self.dp[n-1]
                else:
                    count += self.numTrees(n-1)  
            elif num <= (n+1)//2:
                if num - 1 in self.dp:
                    a = self.dp[num - 1]
                else:
                    a = self.numTrees(num - 1)
                if n-num in self.dp:
                    b = lst[n-num]
                else:
                    b = self.numTrees(n-num)
            
                count += a * b
                x[num] = a * b
                    
            else:
                count += x[n-num+1]
                
      
        if n not in self.dp:
            self.dp[n] = count
            
        return count
            
                
            
        
        
