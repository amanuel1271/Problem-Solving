class Solution:
    def checkvalid(self,lst):
        checklst = [0] * 9
        for i in lst:
            if i != '.':
                if checklst[int(i) - 1]  == 0:
                    checklst[int(i) - 1] = 1
                else:
                    return False
        return True
                
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWSIZE = 9
        COLSIZE = 9
        GRIDSIZE = 9
        
        ##check rows
        for rows in range(ROWSIZE):
            if not self.checkvalid(board[rows]):
                return False
            
        ##check cols
        for col in range(COLSIZE):
            makelst = []
            for rows in range(ROWSIZE):
                makelst.append(board[rows][col])
            if not self.checkvalid(makelst):
                return False
            
        i = 0
        j = 0
        
        for box in range(GRIDSIZE):
            makelst = [ board[3*j][3*i],board[3*j][3*i + 1],board[3*j][3*i + 2],
                      board[3*j + 1][3*i],board[3*j + 1][3*i + 1],board[3*j + 1][3*i + 2], 
                      board[3*j + 2][3*i],board[3*j + 2][3*i + 1],board[3*j + 2][3*i + 2] ]
            
            if not self.checkvalid(makelst):
                return False
            
            i += 1
            i = i % 3
            if  not i:
                j += 1
                
        return True
