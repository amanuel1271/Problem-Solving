class Solution:
    def maximumSwap(self, num: int) -> int:
        strRep = list(str(num))
        maxx = num
        
        for i in range(len(strRep)):
            for j in range(i+1,len(strRep)):
                strRep[i],strRep[j] = strRep[j],strRep[i]
                maxx = max(maxx,int(''.join(strRep)))
                strRep[i],strRep[j] = strRep[j],strRep[i]
        
        return maxx
        
        
        
        
        