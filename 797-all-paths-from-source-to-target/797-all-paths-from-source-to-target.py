class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        
        def dfs(prev_lst,index):
            if index == n:
                self.res.append(prev_lst + [index])
                return
            
            for neighbor in graph[index]:
                dfs(prev_lst + [index],neighbor)
            
            return 
        
        self.res = []
        dfs([],0)
        return self.res
            
            
                
                
            
        
        