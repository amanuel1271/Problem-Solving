class Solution:
    def numIslands(self, grid):
        s,num = set(),0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    s.add((i,j))
            
            
        while s:
            num += 1
            queue = deque([s.pop()])
            while queue:
                i, j = queue.popleft()
                for item in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if item in s:
                        s.remove(item)
                        queue.append(item)
        return num
