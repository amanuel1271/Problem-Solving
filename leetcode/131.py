class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(string):
            size = len(string)
            if size <= 1:
                return True
            
            l,r = 0,size-1
            while l < r:
                if string[l] != string[r]:
                    return False
                l,r = l+1,r-1
            
            return True

        def helper(string,acc):
            size = len(string)
            if size == 0:
                if acc != []:
                    res.append(acc)
                return
            
            for i in range(1,len(string) + 1):
                if isPalindrome(string[:i]):
                    helper(string[i:],acc + [string[:i]])
        
        helper(s,[])
        return res
