

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(list(s1)))
        s2 = ''.join(sorted(list(s2)))
        i1=0
        found = True
        while i1<len(s1) and found:
            if s1[i1]<s2[i1]:
                found = False
            i1+=1
        if not found:
            i2 = 0
            found = True
            while i2<len(s2) and found:
                if s1[i2]>s2[i2]:
                    found = False
                i2+=1
        return found
        
        
                        
        