class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        findprev = self.kthGrammar(n-1,ceil(k/2))
        if k % 2 == 0:
            return 1 - findprev
        else:
            return findprev
        