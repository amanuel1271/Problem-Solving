class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        count_islands = 0
        visited = set()
        row_map,col_map = defaultdict(set),defaultdict(set)
        
        for row,col in stones:
            row_map[row].add((row,col))
            col_map[col].add((row,col))
        
        def dfs(x,y):
            visited.add((x,y))
            for next_x,next_y in row_map[x]:
                if (next_x,next_y) not in visited:
                    dfs(next_x,next_y)
            for next_x,next_y in col_map[y]:
                if (next_x,next_y) not in visited:
                    dfs(next_x,next_y)
                
                
                
        for stone in stones:
            x,y = stone
            if (x,y) not in visited:
                dfs(x,y)
                count_islands += 1
                
            
        return len(stones) - count_islands
                
            
        