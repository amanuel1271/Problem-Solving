class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @lru_cache(None)
        def play(i,j,turn):
            if i > j:
                return 0
            
            option_1 = turn * piles[i] + play(i+1,j,-turn)
            option_2 = turn * piles[j] + play(i,j-1,-turn)
            
            return max(option_1,option_2) if turn == 1 else min(option_1,option_2)
        
        return play(0,len(piles)-1,1)
        