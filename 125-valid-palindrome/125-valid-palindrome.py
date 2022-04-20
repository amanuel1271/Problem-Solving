class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        
        while l <= r:
            if not (s[l].isalpha() or s[l].isdigit()) and (s[r].isalpha() or s[r].isdigit()):
                l += 1
            elif not (s[r].isalpha() or s[r].isdigit()) and (s[l].isalpha() or s[l].isdigit()):
                r -= 1
            elif not (s[r].isalpha() or s[r].isdigit()) and not (s[l].isalpha() or s[l].isdigit()):
                l += 1
                r -= 1
                
            elif (s[r].isalpha() or s[r].isdigit()) and (s[l].isalpha() or s[l].isdigit()):
                if s[l].lower() != s[r].lower():
                    return False
                r -= 1
                l += 1
                
            
        return True
                
        