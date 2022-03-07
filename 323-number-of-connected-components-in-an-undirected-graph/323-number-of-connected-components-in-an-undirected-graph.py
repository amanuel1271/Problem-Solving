class Solution:
    
    def adj_lst_mk(self,edges,n):
            adj_dic = {}
            for i in range(n): 
                adj_dic[i] = []
            for edge in edges:
                for i in range(2):
                    adj_dic[edge[i]].append(edge[1-i])     
            return adj_dic
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_lst = self.adj_lst_mk(edges,n)
        visited,s = set(),set()
        Q = deque()
        count = 0
        
        for i in range(n):
            s.add(i)
            
        while s:
            index = s.pop()
            if index in visited:
                continue
                
            Q.append(index)
            visited.add(index)
            
            while Q:
                vindex = Q.popleft()
                
                for index in adj_lst[vindex]:
                    if index not in visited:
                        Q.append(index)
                        visited.add(index)
            count += 1
        return count
        
        
            
        