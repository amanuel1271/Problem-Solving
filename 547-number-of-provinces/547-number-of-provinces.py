class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n,count = len(isConnected),0
        visited,s = set(),set()
        Q = deque()
        
        for i in range(1,n+1):
            s.add(i)
        
        while s:
            index = s.pop()
            if index in visited:
                continue
                
            Q.append(index)
            visited.add(index)
            
            while Q:
                vindex = Q.popleft()
                
                for index,i in enumerate(isConnected[vindex - 1]):
                    if i == 1 and (index+1) not in visited:
                        Q.append(index+1)
                        visited.add(index+1)
            count += 1
        return count
            
            
                        
                
        