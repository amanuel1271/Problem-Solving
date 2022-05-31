class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        
        for i,ch in enumerate(palindrome):
            if ch == 'a':
                continue
            
            if not (n%2 == 1 and i==n//2):
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:n-1] + 'b'
            
            
        