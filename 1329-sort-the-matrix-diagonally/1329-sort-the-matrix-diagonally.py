class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        Q = deque()
        m,n = len(mat),len(mat[0])
        
        for i in range(n):
            Q.append((0,i))
        for j in range(1,m):
            Q.append((j,0))
        
        while Q:
            x,y = Q.popleft()
            res = []
            
            x_,y_ = x,y
            while 0 <= x_ < m and 0 <= y_ < n:
                res.append(mat[x_][y_])
                x_,y_ = x_ + 1, y_ + 1
                
            res.sort()
            i = 0
            while i < len(res):
                mat[x][y] = res[i]
                i += 1
                x,y = x + 1, y + 1
            
        return mat
        
        