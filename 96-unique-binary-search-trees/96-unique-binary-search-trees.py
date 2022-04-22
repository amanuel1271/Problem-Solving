class Solution:
    def numTrees(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n):
            if n <= 2:
                return n

            count = 0
            for i in range(1,n+1):
                left = helper(i - 1)
                right = helper(n - i)
                
                if left == 0: left = 1
                if right == 0: right = 1
                    
                count += left * right
                
            return count

        return helper(n)
        
        
        