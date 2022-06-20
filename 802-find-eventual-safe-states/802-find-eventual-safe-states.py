class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        unsafe_nodes = set()
        res = []
        
        

        def safe_dfs(start,visited):
            if not graph[start]:
                return True
            elif start in safe_nodes:
                return True
            elif start in unsafe_nodes:
                return False
            
            
            for neighbor in graph[start]:
                if neighbor in visited:
                    unsafe_nodes.add(neighbor)
                    return False
                
                visited.add(neighbor)
                if not safe_dfs(neighbor,visited):
                    unsafe_nodes.add(neighbor)
                    return False
                
                visited.remove(neighbor)
                safe_nodes.add(neighbor)
                
            return True
        
        for k in range(len(graph)):
            if safe_dfs(k,set([k])):
                res.append(k)


        
        return res
                
                
        