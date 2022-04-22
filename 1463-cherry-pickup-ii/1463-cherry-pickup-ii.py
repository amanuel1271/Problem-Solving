class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        @lru_cache(None)
        def traverse(i,j1,j2):
            if i > m-1:
                return 0
            
            coins_collected = 0
            
            if j1 != j2:
                coins_collected += grid[i][j1]
                
            coins_collected += grid[i][j2]
            maxx = 0
            for y1 in [j1,j1+1,j1-1]:
                if 0 <= y1 < n:
                    for y2 in [j2,j2+1,j2-1]:
                        if 0 <= y2 < n:
                            maxx = max(traverse(i+1,y1,y2),maxx)
                                
            coins_collected += maxx
            return coins_collected
        
        
        return traverse(0,0,n-1)
                

                
            
        