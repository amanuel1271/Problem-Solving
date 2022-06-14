class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 1 2 2 4 7 8
        piles.sort()
        left,right,count = 0,len(piles)-1,0
        
        while left < right:
            count += piles[right-1]
            left += 1
            right -= 2
            
        return count
            
        