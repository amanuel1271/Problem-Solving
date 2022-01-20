class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        output = 0
        heap = [(0,0,0)]
        visited = set()
        
        while heap:
            k,x,y = heapq.heappop(heap)

            output = max(output,k)
            
            if (x,y) == (m-1,n-1): 
                break
            visited.add((x,y))
            
            for dx,dy in dirs:
                new_x,new_y = x+dx,y+dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x,new_y) not in visited:
                    new_k = abs(heights[x][y] - heights[new_x][new_y])
                    heapq.heappush(heap,(new_k,new_x,new_y))
                    
        return output
