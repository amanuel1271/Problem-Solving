class Solution:
    def maximumSwap(self, num: int) -> int:
        
        strRep = list(str(num))
        storeIndex = dict()
        
        for i,digit in enumerate(strRep):
            storeIndex[digit] = i
            
        for index in range(len(strRep)):
            for j in range(9,int(strRep[index]),-1):
                if str(j) in storeIndex:
                    swapIndex = storeIndex[str(j)]
                    if swapIndex <= index:
                        continue
                    strRep[index],strRep[swapIndex] = strRep[swapIndex],strRep[index]
                    return int(''.join(strRep))
                
        return num
        
        
        
        
        