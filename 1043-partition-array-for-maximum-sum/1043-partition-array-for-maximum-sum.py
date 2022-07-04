class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @lru_cache(None)
        def maxPartition(n):
            if n == 0:
                return 0
            elif n < k:
                return max(arr[:n]) * n

            max_divide = -math.inf
            max_so_far = arr[n-1]
            for j in range(n-1,n-1-k,-1):
                max_so_far = max(max_so_far,arr[j])
                max_divide = max(max_divide, maxPartition(j) + (n-j) * max_so_far)
                
            return max_divide
                
        
        
        return maxPartition(len(arr))
        