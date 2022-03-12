class Solution:
    def checkValidString(self, s: str) -> bool:
        #dp = { (len(s), 0) : True } # key=(i, leftCount) -> isValid
        @lru_cache(None)
        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            
            
            if s[i] == "(":
                res = dfs(i + 1, left + 1)
            elif s[i] == ")":
                res =  dfs(i + 1, left - 1)
            else:
                res =  (dfs(i + 1, left + 1) or
                                  dfs(i + 1, left - 1) or
                                  dfs(i + 1, left))
            return res
        
        return dfs(0, 0)
                    
            