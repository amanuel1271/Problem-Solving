class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = []
        start,row,col = True,0,0
        
        for ch in s:
            if row == numRows - 1:
                start = False
            elif row == 0:
                start = True
            
            ans.append((row,col,ch))
            if start:
                row += 1
            else:
                row,col = row-1,col+1
                
        res = ''       
        for r,c,ch in sorted(ans):
            res += ch
            
        return res
            
        
        
        