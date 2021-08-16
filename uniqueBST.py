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
        dp_symmetric = {}
        
        for num in range(1,n+1):
            
            if num == 1 or num == n:
                if n-1 in self.dp:
                    count += self.dp[n-1]
                else:
                    count += self.numTrees(n-1)  
                    
            elif num <= (n+1)//2:
                if num - 1 in self.dp:
                    left_count = self.dp[num - 1]
                else:
                    left_count = self.numTrees(num - 1)
                if n-num in self.dp:
                    right_count = self.dp[n-num]
                else:
                    right_count = self.numTrees(n-num)
                count += left_count * right_count
                dp_symmetric[num] = left_count * right_count  
                
            else:
                count += dp_symmetric[n-num+1]
                
        if n not in self.dp:
            self.dp[n] = count
            
        return count
            
                
            
        
        
