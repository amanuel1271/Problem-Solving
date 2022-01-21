class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum_cost = [0] * (len(cost) + 1)
        
        
        for i in range(2, len(cost) + 1):
            minimum_cost[i] = min(minimum_cost[i - 1] + cost[i - 1],minimum_cost[i - 2] + cost[i - 2])


        return minimum_cost[-1]
