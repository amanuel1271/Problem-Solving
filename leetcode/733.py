class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        start_index = (sr,sc)
        visited = {start_index}
        Q = deque([start_index])
        initcolor = image[sr][sc]
        image[sr][sc] = newColor
        
        while Q:
            x,y = Q.popleft()
            for xl,xr in [(x + 1,y),(x - 1,y),(x, y + 1),(x, y - 1)]:
                if (xl,xr) not in visited:
                    if 0 <= xl < m  and 0 <= xr < n:
                        if image[xl][xr] == initcolor:
                            visited.add((xl,xr))
                            Q.append((xl,xr))
                            image[xl][xr] = newColor
        
        return image
