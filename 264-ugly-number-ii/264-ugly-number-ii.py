class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i = j = k = 0
        size = 1
        
        while size < n:
            minn = min(ugly[i] * 2,ugly[j] * 3,ugly[k] * 5)
            
            if minn == ugly[i] * 2:
                i += 1
            if minn == ugly[j] * 3:
                j += 1
            if minn == ugly[k] * 5:
                k += 1
                
            ugly.append(minn)
            size += 1
        

        return ugly[-1]
            
        
        
        
        
        
        
        
        
        
        