class Solution:
    def constructAdjList(self,equations,values):
        adjLst = defaultdict(list)
        for index,pair in enumerate(equations):
                adjLst[pair[0]].append((pair[1],values[index])) 
                adjLst[pair[1]].append((pair[0],1/values[index]))
        return adjLst
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        self.visited = set()
        self.val = float(-1)
        self.adjLst = self.constructAdjList(equations,values)
        
        def dfs(self,start,end,acc):
            self.visited.add(start)
            if end == start:
                self.val = acc
                return True
            
            for neighbors in self.adjLst[start]:
                if (neighbors[0] not in self.visited and dfs(self,neighbors[0],end,acc * neighbors[1])):
                    return True
            return False
            
        res = [float(-1) for j in range(len(queries))]
        for index,pair in enumerate(queries):
            if pair[0] not in self.adjLst or pair[1] not in self.adjLst:
                continue  
            if dfs(self,pair[0],pair[1],float(1)):
                res[index] = self.val
            self.visited = set()
        
        return res
            
        
        
        
        
                
        