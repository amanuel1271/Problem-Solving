class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        
        def dfs(row,col,i, path):
            if i == len(word) - 1 and word[i] == board[row][col]:
                return True
            
            
            for (r,c) in [(row,col+1), (row+1, col), (row-1, col), (row, col-1)]:
                if not(0 <= r < m and 0 <= c < n) or (r,c) in path or i < len(word) - 1 and word[i+1] != board[r][c] :
                    continue
                path.add((r,c))
                if dfs(r,c,i+1,path):
                    return True
                path.remove((r,c))
            return False

        starting_place = [(r,c) for r in range(m) for c in range(n) if word[0] == board[r][c]]
        return any(list(map(lambda x: dfs(x[0],x[1],0,{x}), starting_place)))
