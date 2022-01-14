class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def constructAdjList(equations,values):
            adjLst = {}
            for index,pair in enumerate(equations):
                if pair[0] in adjLst:
                    adjLst[pair[0]].append((pair[1],values[index]))
                else:
                    adjLst[pair[0]] = [(pair[1],values[index])]
                
                if pair[1] in adjLst:
                    adjLst[pair[1]].append((pair[0],1/values[index]))
                else:
                    adjLst[pair[1]] = [(pair[0],1/values[index])]
            return adjLst
        
        self.visited = set()
        self.val = math.inf
        self.adjLst = constructAdjList(equations,values)
        
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
        print(self.adjLst)
        for index,pair in enumerate(queries):
            if pair[0] not in self.adjLst or pair[1] not in self.adjLst:
                continue
                
            if dfs(self,pair[0],pair[1],float(1)):
                res[index] = self.val
            
            self.visited = set()
        
        return res
