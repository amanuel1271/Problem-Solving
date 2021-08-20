class Solution:
    def __init__(self):
        self.dp = {}
        self.dp[1] = 1
        self.dp[2] = 2 
        
    def search_dict(self,i):
        if i in self.dp:
            return self.dp[i]
        return self.numTrees(i)
        
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        
        count = 0
        dp_symmetric = {}
        
        for num in range(1,n+1):
            if num == 1 or num == n:
                count += self.search_dict(n-1) 
                
            elif num <= (n+1)//2:
                left_count = self.search_dict(num - 1)
                right_count = self.search_dict(n - num)
                count += left_count * right_count
                dp_symmetric[num] = left_count * right_count    
            else:
                count += dp_symmetric[n-num+1]
                
        if n not in self.dp:
            self.dp[n] = count
            
        return count
            
                
            
        
        
