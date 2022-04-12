class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        size = len(s)
        
        @lru_cache(None)
        def move(i,prev):
            if i == size:
                return 0
            
            ith = int(s[i])
            flip = (ith + 1) % 2
            
            if prev == '' or prev == '0':
                return min(1 + move(i+1,str(flip)),move(i+1,str(ith)))
            
            if ith == 1:
                return move(i+1,'1')
            else:
                return 1 + move(i+1,'1')
            
        
        return move(0,'')
            
                
            
        