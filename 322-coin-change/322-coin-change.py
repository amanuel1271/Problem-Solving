class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = set(coins) # dont care about dup
        
        @lru_cache(None)
        def dp(amt):
            if amt in coins:
                return 1
            elif amt <= 0:
                return amt
            
            minn = math.inf
            
            for coin in coins:
                res = dp(amt-coin)
                if res <  0:
                    continue
                    
                minn = min(minn,res)
            
            return minn + 1 if minn != math.inf else -1
            
    
        
        return dp(amount)
                
        
            
                
                
            
            
            
            
        