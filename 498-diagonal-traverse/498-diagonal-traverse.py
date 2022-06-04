class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        reverse,m,n = 0,len(mat),len(mat[0])
        Q = deque([(r,0) for r in range(m)] + [(m-1,c) for c in range(1,n)])
        
        while Q:
            row,col = Q.popleft()
            diag_lst = []
            while 0 <= row < m and 0 <= col < n:
                diag_lst.append(mat[row][col])
                row -= 1
                col += 1
            if reverse:
                res.extend(list(reversed(diag_lst)))
            else:
                res.extend(diag_lst)
                
            reverse = 1 - reverse
                
        return res