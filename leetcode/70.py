class Solution:
    def climbStairs(self, n: int) -> int:
        def climbcache(n,cache):
            
            def getcache(i,cache):
                if i in cache:
                    return cache[i]
                cache[i] = climbcache(i,cache)
                return cache[i]
                
            if n in cache:
                return cache[n]
            
            cache[n] = getcache(n-1,cache) + getcache(n-2,cache)
            return cache[n]
            
            
        return climbcache(n,{1:1,2:2})
