class Solution:
    def numTrees(self, n: int) -> int:
        
        def helper(n,dic):
            if n in dic:
                return dic[n]

            count = 0
            for i in range(1,n+1):
                if i-1 in dic:
                    left = dic[i - 1] 
                else:
                    left = helper(i - 1,dic)
                if n - i in dic:
                    right = dic[n-i]
                else:
                    right = helper(n - i,dic)
    
                
                if left == 0: left = 1
                if right == 0: right = 1
                    
                count += left * right
                
            dic[n] = count
            return count
        
        dic = {0:0,1:1,2:2}
        return helper(n,dic)
        
        
        