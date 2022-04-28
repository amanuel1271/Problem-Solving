class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        size = len(piles)
        
        @lru_cache(None)
        def play(i,j):
            if i > j:
                return 0
            
            turn = size - (j-i+1)
            
            option_1 = turn * piles[i] + play(i+1,j)
            option_2 = turn * piles[j] + play(i,j-1)
            
            return max(option_1,option_2) if turn % 2 == 0 else min(option_1,option_2)
        
        return play(0,len(piles)-1)
        