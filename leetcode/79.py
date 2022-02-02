class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        
        def dfs(x,y,i,path):
            if i == len(word)-1:
                return True
            for xl,xr in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0 <= xl < m and 0 <= xr < n and (xl,xr) not in path:
                    if board[xl][xr] == word[i+1]:
                        if dfs(xl,xr,i+1,set.union(path,{(x,y)})):
                            return True
            return False
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0,set()):
                        return True
        
        return False
