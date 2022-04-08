class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.first_row = [0 for _ in range(n)]
        self.first_col = [0 for _ in range(n)]
        self.first_pos_diag = [0]
        self.first_neg_diag = [0]
        
        self.second_row = [0 for _ in range(n)]
        self.second_col = [0 for _ in range(n)]
        self.second_pos_diag = [0]
        self.second_neg_diag = [0]

    def move(self, row: int, col: int, player: int) -> int:
        
        def player_move(p_row,p_col,pos_diag,neg_diag,p):
            p_row[row] += 1
            p_col[col] += 1
            if row + col == self.n - 1:
                pos_diag[0] += 1
            if row == col:
                neg_diag[0] += 1
                

            return p if (p_row[row] == self.n or p_col[col] == self.n or pos_diag[0] == self.n or neg_diag[0] == self.n) else 0
        
        print(self.first_row)
        print(self.second_row)
        
        if player == 1:
            return player_move(self.first_row,self.first_col,self.first_pos_diag,self.first_neg_diag,1)
        else:
            return player_move(self.second_row,self.second_col,self.second_pos_diag,self.second_neg_diag,2)
            
                
        
                
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)