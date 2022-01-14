class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        
        def dfs(prev_lst,index,n):
            if index == n:
                self.res.append(prev_lst + [index])
                return
            
            for neighbor in graph[index]:
                dfs(prev_lst + [index],neighbor,n)
            
            return 
        
        self.res = []
        dfs([],0,n)
        return self.res
