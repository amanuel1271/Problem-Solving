class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = ''
        for ch in s:
            if ch.isalpha():
                alpha_num += ch.lower()
            elif ch.isdigit():
                alpha_num += ch
                
        
        l,r = 0,len(alpha_num)-1
        
        while l <= r:
            if alpha_num[l] != alpha_num[r]:
                return False
            r -= 1
            l += 1
            
        return True
                
        