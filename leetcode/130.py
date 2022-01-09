class Solution:

    def solve(self, board):
        borderset = set() #set to hold the border O's
        visited = set() # to track the O's that are not captured
        
        m,n = len(board),len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m-1):
                    borderset.add((i,j))
                elif board[i][j] == 'O' and (j == 0 or j == n-1):
                    borderset.add((i,j))
        
        while borderset:
            bx,by = borderset.pop()
            Q = deque([(bx,by)])
            visited.add((bx,by))
            
            while Q:
                x,y = Q.popleft()
                for xl,xr in [(x + 1,y),(x - 1,y),(x, y - 1),(x, y + 1)]:
                    if 0 <= xl < m and 0 <= xr < n:
                        if board[xl][xr] == 'O' and (xl,xr) not in visited:
                            Q.append((xl,xr))
                            visited.add((xl,xr))
                            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
