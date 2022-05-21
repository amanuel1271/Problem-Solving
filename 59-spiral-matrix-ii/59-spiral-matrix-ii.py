class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[math.inf for _ in range(n)] for _ in range(n)]
        ori = 'E'
        next_ori = {'E':'S','S':'W','W':'N','N':'E'}
        move = {'E':(0,1),'S':(1,0),'W':(0,-1),'N':(-1,0)}
        row_pos,col_pos = 0,0
        
        res[0][0] = 1
        
        for count in range(2,n*n+1):
            dx,dy = move[ori]
            row_pos,col_pos = row_pos + dx ,col_pos  + dy
            if not (0 <= row_pos < n and 0 <= col_pos < n and res[row_pos][col_pos] == math.inf):
                row_pos,col_pos = row_pos - dx,col_pos  - dy
                ori = next_ori[ori]
                dx,dy = move[ori]
                row_pos,col_pos = row_pos + dx ,col_pos  + dy

            res[row_pos][col_pos] = count
                
        return res
                
                        
        
        
        