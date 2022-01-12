class Solution:     
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        adj_lst = {}
        for i in range(n):
            adj_lst[i] = []
        
        logs.sort(key=lambda x:x[0]) # sort by timestamp
        for event in logs:
            timestamp,vertice1,vertice2 = event[0],event[1],event[2]
            adj_lst[vertice1].append(vertice2)
            adj_lst[vertice2].append(vertice1)
            
            visited = {vertice1}
            Q = deque([vertice1])
            
            while Q:
                v = Q.popleft()
                for neighbor in adj_lst[v]:
                    if neighbor not in visited:
                        Q.append(neighbor)
                        visited.add(neighbor)
                        
            if len(visited) == n:
                return timestamp
            
        return -1
