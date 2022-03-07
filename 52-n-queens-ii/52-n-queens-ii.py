class Solution:
    def totalNQueens(self, n: int) -> int:
        col,posDiag,negDiag = set(),set(),set()
        self.count = 0
        
        
        def backtrack(r):
            if r == n:
                self.count += 1
             
            for c in range(n):
                if c in col or r+c in negDiag or r-c in posDiag:
                    continue
                
                col.add(c)
                posDiag.add(r-c)
                negDiag.add(r+c)
                
                backtrack(r+1)
                
                col.remove(c)
                posDiag.remove(r-c)
                negDiag.remove(r+c)
        
        backtrack(0)
        return self.count
                
                
                
        