class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0
        
        for amt in range(amount+1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt],dp[amt-coin] + 1)
                    
        
        return -1 if dp[amt] == math.inf else dp[amt]
                
        
            
                
                
            
            
            
            
        