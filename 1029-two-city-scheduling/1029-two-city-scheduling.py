class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        
        @lru_cache(None)
        def visit(i,num_of_a):
            if i >= 2*n:
                return 0
            
            if num_of_a == n:
                res = costs[i][1] + visit(i+1,num_of_a)
            elif i - num_of_a == n:
                res = costs[i][0] + visit(i+1,num_of_a + 1)
            else:
                res = min(costs[i][0] + visit(i+1,num_of_a + 1),costs[i][1] + visit(i+1,num_of_a))
            
            return res
        
        return visit(0,0)
        
        