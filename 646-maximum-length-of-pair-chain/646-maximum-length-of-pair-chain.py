class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = -math.inf, 0
        
        for x, y in sorted(pairs, key = lambda x: x[1]): 
            if cur < x:
                cur = y
                ans += 1
                
        return ans
        
