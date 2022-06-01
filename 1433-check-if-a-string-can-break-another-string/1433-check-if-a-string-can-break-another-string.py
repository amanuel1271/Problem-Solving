

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def canbreak(s1,s2):
            count = [0]*26
            for ch in s1:
                count[ord(ch) - ord('a')] += 1
                
            for ch in s2:
                found_bigger = False
                
                #O(1) because it loops at most 26 times
                for i in range(ord(ch) - ord('a'),26):
                    if count[i] > 0:
                        found_bigger = True
                        count[i] -= 1
                        break
                if not found_bigger:
                    return False
                
            return True
        
        
        return canbreak(s1,s2) or canbreak(s2,s1)
        
        
                        
        