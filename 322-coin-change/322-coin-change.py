class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = set(coins) # dont care about dup
        
        @lru_cache(None)
        def dp(amt):
            if amt < 0:
                return math.inf
            elif amt == 0:
                return 0
            elif amt in coins:
                return 1
            
            minn = math.inf
            
            for coin in coins:       
                minn = min(minn,1 + dp(amt-coin))
            
            return minn
            
    
        ans = dp(amount)
        return ans if ans != math.inf else -1
                
        
            
                
                
            
            
            
            
        