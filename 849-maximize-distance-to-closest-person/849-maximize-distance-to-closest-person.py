class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        while i < len(seats) and seats[i] == 0:
            i += 1
            
        j = len(seats)-1
        while j >= 0 and seats[j] == 0:
            j -= 1
            
        res = max(i,len(seats)-1-j)
        
        is_zero,zeroes = False,0
        for i in range(len(seats)):
            if seats[i] == 1:
                is_zero = False
                res = max(res,math.ceil(zeroes/2))
                zeroes = 0
            else:
                zeroes += 1
        
        return res
                
            
            
        