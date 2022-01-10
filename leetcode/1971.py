class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        def helper(start,end,visited):
            if [start,end]  in edges or [end,start] in edges:
                return True

            for edge in edges:
                if edge[0] == start and edge[1] not in visited:
                    visited.add(edge[1])
                    if helper(edge[1],end,visited):
                        return True
                elif edge[1] == start and edge[0] not in visited:
                    visited.add(edge[0])
                    if helper(edge[0],end,visited):
                        return True
                    
            
            return False
        
        if start > n:
            return False
        elif not edges and start == end:
            return True
        visited = set()
        visited.add(start)
        return helper(start,end,visited)
        
