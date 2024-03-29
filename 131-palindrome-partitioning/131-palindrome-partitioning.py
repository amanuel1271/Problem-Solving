class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        @lru_cache(None)
        def isPalindrome(string):
            size = len(string)
            l,r = 0,size-1
            
            while l <= r:
                if string[l] != string[r]:
                    return False
                l,r = l+1,r-1
            return True

        def dfs(string,acc):
            size = len(string)
            if size == 0:
                if acc != []:
                    res.append(acc)
                return
            
            for i in range(1,len(string) + 1):
                if isPalindrome(string[:i]):
                    dfs(string[i:],acc + [string[:i]])
        
        dfs(s,[])
        return res
                    
                
                
        