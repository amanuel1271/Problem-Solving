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
            makelst = [board[rows][col] for rows in range(ROWSIZE)]
            if not self.checkvalid(makelst):
                return False  
            
        i = 0
        j = 0
        for box in range(GRIDSIZE):
            makelst = [board[3*j + row][3*i + col] for row in range(ROWSIZE//3) for col in range(COLSIZE//3)]
            if not self.checkvalid(makelst):
                return False
            i += 1
            i %= 3
            if i == 0:
                j += 1
                
        return True
        