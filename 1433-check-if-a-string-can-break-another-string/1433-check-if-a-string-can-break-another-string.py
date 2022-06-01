class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        count1,count2 = [0]*26,[0]*26
        for ch in s1:
                count1[ord(ch) - ord('a')] += 1
        for ch in s2:
                count2[ord(ch) - ord('a')] += 1
        
        def canbreak(s1,s2,count):
            for ch in s2:
                found_bigger = False
                for i,cnt in enumerate(count):
                    if i >= ord(ch) - ord('a') and cnt > 0:
                        found_bigger = True
                        count[i] -= 1
                        break
                if not found_bigger:
                    return False 
            return True
        
        
        return canbreak(s1,s2,count1) or canbreak(s2,s1,count2)
        
        
                        
        