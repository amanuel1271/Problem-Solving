class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def adjList():
            adjDic = {}
            for i in range(n):
                adjDic[i] = []
            for pair in edges:
                adjDic[pair[0]].append(pair[1])
                
            return adjDic
        
        self.adj = adjList() 
            
        def dfs(src,path):
            if self.adj[src] == []:
                if src != destination:
                    return False
                return True
            
            
            for neib in self.adj[src]:
                if src in path or not dfs(neib,path + [src]):
                    return False
            
            return True
        
        return dfs(source,[])
            
        
        
        