class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        size = len(values)
        maxx,maxend = -math.inf,values[size-1]-(size-1)
        
        for i in range(size-2,-1,-1):
            maxend = max(maxend,values[i+1]-(i+1))
            maxx = max(maxx,values[i]+i+maxend)
            
        return maxx