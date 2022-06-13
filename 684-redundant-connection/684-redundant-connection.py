class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.adj = defaultdict(list)
        
        def dfs(start,end):
            if start == end:
                return True
            
            for neighbor in self.adj[start]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor,end):
                        return True
            return False
        
        for edge in edges:
            visited = set()
            if dfs(edge[0],edge[1]):
                return edge
            
            self.adj[edge[0]].append(edge[1])
            self.adj[edge[1]].append(edge[0])

            
        