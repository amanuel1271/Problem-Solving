class Solution:
    def solveNQueens(self, n):
        col,posDiag,negDiag = set(),set(),set()
        ans = []
        res = [['.' for _ in range(n)] for _ in range(n)]
        
        
        def backtrack(r):
            if r == n:
                ans.append([''.join(row) for row in res])
                return
             
            for c in range(n):
                if c in col or r+c in negDiag or r-c in posDiag:
                    continue
                
                col.add(c)
                res[r][c] = 'Q'
                posDiag.add(r-c)
                negDiag.add(r+c)
                
                backtrack(r+1)
                
                col.remove(c)
                res[r][c] = '.'
                posDiag.remove(r-c)
                negDiag.remove(r+c)
        
        backtrack(0)
        return ans
        