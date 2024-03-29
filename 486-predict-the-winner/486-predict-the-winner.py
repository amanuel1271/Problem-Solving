class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        size = len(nums)

        
        @lru_cache(None)
        def player_1_profit(i,j,turn):
            if j == i:
                return turn * nums[j]
            
            move_1 = turn * nums[i] + player_1_profit(i+1,j,-1 * turn)
            move_2 = turn * nums[j] + player_1_profit(i,j-1,-1 * turn)
            
            return max(move_1,move_2) if turn == 1 else min(move_1,move_2)
                
        

        return player_1_profit(0,size-1,1) >= 0
                
                
            
            
        