class Solution:
    def maximumSwap(self, num: int) -> int:
        strRep = list(str(num))
        size = len(strRep)
        maxx = num
        
        for i in range(size):
            for j in range(i+1,size):
                strRep[i],strRep[j] = strRep[j],strRep[i]
                maxx = max(maxx,int(''.join(strRep)))
                strRep[i],strRep[j] = strRep[j],strRep[i]
        
        return maxx
        
        
        
        
        