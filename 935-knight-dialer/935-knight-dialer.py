class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        
        adj = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
        
        @lru_cache(None)
        def dfs(start,length):
            if length == 1:
                return 1
            
            count  = 0
            for nei in adj[start]:
                count += dfs(nei,length-1)
                
            return count
        
        ans = 0
        for starting in adj:
            ans += dfs(starting,n)
            
        return ans%MOD
            
        
        