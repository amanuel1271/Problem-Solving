class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        
        while l <= r:
            if not (s[l].isalnum()) and (s[r].isalnum()):
                l += 1
            elif not (s[r].isalnum()) and (s[l].isalnum()):
                r -= 1
            elif not (s[r].isalnum()) and not (s[l].isalnum()):
                l += 1
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                r -= 1
                l += 1
                
            
        return True
                
        