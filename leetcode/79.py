class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        m,n = len(board),len(board[0])
        
        start_set = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start_set.add((i,j,0))
                    
        def dfs(x,y,i,path):
            if i == word_len-1:
                return True
            for xl,xr in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0 <= xl < m and 0 <= xr < n and (xl,xr) not in path:
                    if board[xl][xr] == word[i+1]:
                        if dfs(xl,xr,i+1,set.union(path,{(x,y)})):
                            return True
            return False
        
        while start_set:
            i,j,index = start_set.pop()
            if dfs(i,j,index,set()):
                return True
        return False
