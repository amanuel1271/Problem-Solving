class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        front,back = 0,0
        
        for i in range(2, len(cost) + 1):
            front,back = min(front + cost[i - 1],back + cost[i - 2]),front
            
        return front
        
        