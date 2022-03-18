class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            
            min_val = math.inf
            for k in range(i, j):
                
                left_max = max(arr[i:k+1])
                right_max = max(arr[k+1:j+1])

                min_val = min(min_val,  left_max * right_max  + dp(i, k) + dp(k+1, j))

            return min_val
        
        return dp(0, len(arr)-1)