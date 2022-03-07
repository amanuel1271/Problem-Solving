

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        Q = deque()
        visited = set()
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    Q.append((i,j))
                    visited.add((i,j))
                    
        
        while Q:
            lenn = len(Q)
            visit = False
            for i in range(lenn):
                xl,yl = Q.popleft()
                for x,y in [(xl+1,yl),(xl-1,yl),(xl,yl-1),(xl,yl+1)]:
                    if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                        if grid[x][y] == 1:
                            Q.append((x,y))
                            visited.add((x,y))
                            visit = True
            if visit:
                count += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1


        
        return count
                
        