class ShipGame:
    def __init__(self):
        self.first_board = [['' for i in range(10)] for j in range(10)]
        self.second_board = [['' for i in range(10)] for j in range(10)]
        self.turn = 'FIRST'
        self.num_ships_first = 0
        self.num_ships_second = 0
        self.state = 'UNFINISHED'
        self.ship1row = dict()
        self.ship1col = dict()
        self.ship2col = dict()
        self.ship2row = dict()

        
    def place_ship(self,player,length,closest,ori): 
        if length < 2:
            return False
        
        row,col = ord(closest[0]) - ord('A'), ord(closest[1]) - ord('1')
        visited = set()

        def check_and_place(board,row_dic,col_dic):
            if ori == 'C':
                if row + length > 10:
                    return False
                
                for r in range(row,row+length):
                    if board[r][col] == 'x':
                        return False
                    board[r][col] = 'x'
                    visited.add(r)

                col_dic[col] = visited
                

            else:
                if col + length > 10:
                    return False
                
                for c in range(col,col+length):
                    if board[row][c] == 'x':
                        return False
                    board[row][c] = 'x'
                    visited.add(c)
                
                row_dic[row] = visited

            return True


        if player == 'first':
            is_ship = check_and_place(self.first_board,self.ship1row,self.ship1col)
            if is_ship:
                self.num_ships_first += 1
        else:
            is_ship = check_and_place(self.second_board,self.ship2row,self.ship2col)
            if is_ship:
                self.num_ships_second += 1

        return is_ship

        
            
            

    def get_current_state(self):
        return self.state

    def fire_torpedo(self,player,coor):
        if self.turn != player:
            return False
        if self.get_current_state() != 'UNFINISHED':
            return False
        
        row,col = ord(coor[0]) - ord('A'), ord(coor[1]) - ord('1')

        if player == 'first':

            if col in self.ship2col and row in self.ship2col[col]:
                self.ship2col[col].remove(row)

                if len(self.ship2col[col]) == 0:
                    self.num_ships_second -= 1

            elif row in self.ship2row and col in self.ship2row[row]:
                self.ship2row[row].remove(col)

                if len(self.ship2row[row]) == 0:
                    self.num_ships_second -= 1


            if self.num_ships_second == 0:
                self.state = 'FIRST_WON'

            self.turn = 'second'

        else:

            if col in self.ship1col and row in self.ship1col[col]:
                self.ship1col[col].remove(row)

                if len(self.ship1col[col]) == 0:
                    self.num_ships_first -= 1

            elif row in self.ship1row and col in self.ship1row[row]:
                self.ship1row[row].remove(col)

                if len(self.ship1row[row]) == 0:
                    self.num_ships_first -= 1
            

            if self.num_ships_first == 0:
                self.state = 'SECOND_WON'

            self.turn = 'first'
        
        return True

                    

    def get_num_ships_remaining(self,player):#
        return self.num_ships_first if player == 'first' else self.num_ships_second






def test():
    game = ShipGame()
    game.place_ship('first', 5, 'B2', 'C')
    game.place_ship('first', 2, 'I8', 'R')
    game.place_ship('second', 3, 'H2', 'C')
    game.place_ship('second', 2, 'A1', 'C')
    game.place_ship('first', 8, 'H2', 'R')
    game.fire_torpedo('first', 'H3')
    game.fire_torpedo('second', 'A1')
    print(game.get_current_state())

test()
