class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        while i < len(seats) and seats[i] == 0:
            i += 1
            
        m = len(seats)-1
        while m >= 0 and seats[m] == 0:
            m -= 1
            
        res = max(i,len(seats)-1-m)
        
        is_zero,zeroes = False,0
        for i in range(len(seats)):
            if seats[i] == 1:
                is_zero = False
                res = max(res,math.ceil(zeroes/2))
                zeroes = 0
            else:
                zeroes += 1
        
        return res
                
            
            
        