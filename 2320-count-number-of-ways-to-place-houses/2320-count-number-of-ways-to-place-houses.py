class Solution:
    def countHousePlacements(self, n: int) -> int:
        
        @lru_cache(None)
        def dfs(i,can_place):
            if i == n+1:
                return 1
            if not can_place:
                return dfs(i+1,True)
            
            return dfs(i+1,False) + dfs(i+1,True)
        
        ans = dfs(1,True)
        
        return (ans ** 2) % (10**9+7)
        