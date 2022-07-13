class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        is_there_queen = [[0]* 8 for _ in range(8)]
        for q in queens:
            is_there_queen[q[0]][q[1]] = 1
            
        ans = []
            
        for x_step,y_step in  [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]:
            for step in range(1,8):
                cur_dir_x,cur_dir_y = king[0] + step * x_step,king[1] + step * y_step
                if cur_dir_x < 0 or cur_dir_x > 7 or cur_dir_y < 0 or cur_dir_y > 7:
                    break #out of bounds
                    
                if is_there_queen[cur_dir_x][cur_dir_y]:
                    ans.append([cur_dir_x,cur_dir_y])
                    break
                
        return ans
                
        
        
        