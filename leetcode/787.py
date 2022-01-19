class Solution:
    def adjList(self,flights):
        adj = defaultdict(list)
        
        for from_,to_,cost in flights:
            adj[to_].append((from_,cost))
        
        return adj
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[math.inf for col in range(n)] for row in range(k+2)]
        adj = self.adjList(flights)
        dp[0][src] = 0
        
        for i in range(1,len(dp)):
            for j in range(len(dp[i])):
                if j == src:
                    dp[i][src] = 0
                    continue
                else:
                    for from_,cost in adj[j]:
                        dp[i][j] = min(dp[i][j],dp[i-1][j],dp[i-1][from_] + cost)
            
                    
        return dp[k+1][dst] if dp[k+1][dst] != math.inf else -1
