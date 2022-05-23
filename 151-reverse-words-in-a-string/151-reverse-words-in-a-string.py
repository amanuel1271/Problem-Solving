class Solution:
    def reverseWords(self, s: str) -> str:
        ans,words = '',s.split()[::-1]
        size = len(words)
        
        for i in range(size):
            ans += words[i]
            if i != size - 1:
                ans += ' '
            
        return ans