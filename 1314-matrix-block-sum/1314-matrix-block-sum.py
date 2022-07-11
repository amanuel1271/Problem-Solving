class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        row_prefix_sum = [[0]*n for _ in range(m+1)]
        
        for r in range(1,m+1):
            for c in range(n):
                row_prefix_sum[r][c] = row_prefix_sum[r-1][c] + mat[r-1][c]
                
        
        ans = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                top,bottom = max(r-k,0),min(m-1,r+k) + 1
                for col in range(max(0,c-k),min(n-1,c+k)+1):
                    ans[r][c] += row_prefix_sum[bottom][col] - row_prefix_sum[top][col]
                    
        return ans
        