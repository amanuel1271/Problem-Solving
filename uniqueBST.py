class Solution:
    def __init__(self):
        self.dp = {}
        self.dp[1] = 1
        self.dp[2] = 2
        
    def memoize(self,n,num,lst,x,count):
        if num - 1 in lst:
            a = lst[num-1]
        else:
            a = self.numTrees(num - 1)
        if n-num in lst:
            b = lst[n-num]
        else:
            b = self.numTrees(n-num)
            
        count += a * b
        x[num] = a * b
            
        return count
        
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
            elif n % 2 == 0 and num <= n//2: # n is even 
                count = self.memoize(n,num,self.dp,x,count)
            elif n % 2 == 0 and num > n//2:
                count += x[n - num + 1]
            elif n % 2 == 1 and num <= (n+1)//2:
                count = self.memoize(n,num,self.dp,x,count)
            elif n % 2 == 1 and num > (n+1)//2:
                count += x[n-num+1]
                
      
        if n not in self.dp:
            self.dp[n] = count
            
        return count
            
                
            
        
        
