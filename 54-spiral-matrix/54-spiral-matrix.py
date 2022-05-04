class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        visited = set()
        next_orientation = {
            'E' : 'S',
            'S' : 'W',
            'W' : 'N',
            'N' : 'E'
        }
        move = {
            'E' : (0,1),
            'S' : (1,0),
            'W' : (0,-1),
            'N' : (-1,0)
            
        }
        pos = (0,0)
        orientation = 'E'
        res = []
        
        while True:
            visited.add(pos)
            res.append(matrix[pos[0]][pos[1]])
            nextx,nexty = pos[0] + move[orientation][0],pos[1] + move[orientation][1]
            if (0 <= nextx < m and 0 <= nexty < n) and (nextx,nexty) not in visited:
                pos = (nextx,nexty)
            else:
                orientation = next_orientation[orientation]
                nextx,nexty = pos[0] + move[orientation][0],pos[1] + move[orientation][1]
                if (0 < nextx < m and 0 <= nexty < n) and (nextx,nexty) not in visited:
                    pos = (nextx,nexty)
                else:
                    break       
        return res
                
                
            
            
        
        