class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(dice_num,target):
            if dice_num == 1:
                return 1 if 1 <= target <= k else 0
            
            count = 0
            for faces in range(1,k+1):
                count += dp(dice_num-1,target-faces)
                
            return count
        
                
        return dp(n,target) % MOD
