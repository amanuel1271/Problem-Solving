class Solution:
    def toAdjLst(self,pairs,slen):
        adjList = defaultdict(list)
        for pair in pairs:
            adjList[pair[0]].append(pair[1])
            adjList[pair[1]].append(pair[0]) 
        return adjList
               
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        slen = len(s)
        resStr = ['0' for i in range(slen)]
        adjList = self.toAdjLst(pairs,slen)
        sset = set()
        checked = set()
        for j in range(slen):
            sset.add(j)
            
        
        while sset:
            index = sset.pop() 
            Q = deque([index])
            visited = {index}
            component = []
            compStr = []
            
            while Q:
                j = Q.popleft()
                component.append(j)
                compStr.append(s[j])
                
                for neighbor in adjList[j]:
                    if neighbor not in visited:
                        Q.append(neighbor)
                        visited.add(neighbor)
                        sset.remove(neighbor)
                        
            component.sort()
            compStr.sort()
            
            for j in range(len(component)):
                resStr[component[j]] = compStr[j]
                
        return ''.join(resStr)
            
                
                
                
                
            
            
            
            
        
        