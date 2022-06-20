class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        res = []
        
        

        def safe_dfs(start,visited):
            if not graph[start]:
                return True
            elif start in safe_nodes:
                return True
            
            
            for neighbor in graph[start]:
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                if not safe_dfs(neighbor,visited):
                    return False
                visited.remove(neighbor)
                safe_nodes.add(neighbor)
                
            return True
        
        for i in range(len(graph)):
            if i in safe_nodes or safe_dfs(i,set([i])):
                res.append(i)
            #print(i,safe_nodes)

        
        return res
                
                
        