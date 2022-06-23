class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            res = 0
            for num in piles:
                res += math.ceil(num/k)
            return res <= h
            
        
        
        l,r = 1,max(piles)
        ans = -1
        
        while l <= r:
            mid = (l+r)//2
            if can_eat(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
                
        return ans
                
        