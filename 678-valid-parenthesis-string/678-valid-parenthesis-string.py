class Solution:
    def checkValidString(self, s: str) -> bool:

        @lru_cache(None)
        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            
            
            if s[i] == "(":
                return dfs(i + 1, left + 1)
            elif s[i] == ")":
                return dfs(i + 1, left - 1)
            else:
                return (dfs(i + 1, left + 1) or
                                  dfs(i + 1, left - 1) or
                                  dfs(i + 1, left))
        
        return dfs(0, 0)
                    
            