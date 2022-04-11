class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len,max_str = 0,''
        s_size = len(s)
        
        #aba abba
        
        for mid in range(s_size):
            l,r = mid-1,mid+1
            
            if max_len == 0:
                max_len = 1
                max_str = s[mid]
            
            while l >= 0 and r < s_size:
                if s[l] != s[r]:
                    break
                if r-l+1 > max_len:
                    max_len,max_str = r-l+1,s[l:r+1]
                l,r = l-1,r+1
                
            l,r = mid,mid+1
            while l >= 0 and r < s_size:
                if s[l] != s[r]:
                    break
                if r-l+1 > max_len:
                    max_len,max_str = r-l+1,s[l:r+1]
                l,r = l-1,r+1
            
            
        
        return max_str 