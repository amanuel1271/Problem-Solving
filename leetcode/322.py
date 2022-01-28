class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = list(set(coins)) # dont care about dup
        
        @lru_cache(None)
        def dp(amt):
            if amt == 0:
                return 0
            elif amt < 0:
                return -1
            
            minn = math.inf
            
            for coin in coins:
                res = dp(amt-coin)
                if res == -1:
                    continue
                minn = min(minn,res)
            
            return minn + 1 if minn != math.inf else -1
            
    
        
        return dp(amount)
