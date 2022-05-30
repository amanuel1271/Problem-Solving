class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        

        @lru_cache(None)
        def dfs(j): 
            if j == n:
                return 0
            
            minn = math.inf
            for i in range(j,n):
                if isPalindrome(j,i):
                    minn = min(dfs(i+1) + 1,minn)
                           
            return minn
        
        return dfs(0) - 1
        