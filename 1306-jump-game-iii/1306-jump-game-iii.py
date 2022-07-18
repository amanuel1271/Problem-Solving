class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        
        @lru_cache(None)
        def dfs(i):
            if i < 0 or i >= len(arr):
                return False
            elif arr[i] == 0:
                return True
            
            if i in visited:
                return False
            
            visited.add(i)
            return dfs(i-arr[i]) or dfs(i+arr[i])
        
        return dfs(start)

            
                