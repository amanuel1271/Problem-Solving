class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        seen = set([(0,0)])
        Q = deque([(0,0,0)])
        
        dir = [(1,2),(2,1),(-1,2),(-2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)]
        
        while Q:
            steps,row,col = Q.popleft()
            if (row,col) == (x,y):
                return steps
            for dx,dy in dir:
                if (row+dx,col+dy) not in seen:
                    seen.add((row+dx,col+dy))
                    Q.append((steps + 1,row+dx,col+dy))
                    
        return -1
                    
            
                    
        
        
        