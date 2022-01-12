class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def adj_lst_mk(edges,n):
            adj_dic = {}
            for i in range(n): # there might be a node with no edge so it is better to make sure every node val is in the dict
                adj_dic[i] = []

            for edge in edges:
                for i in range(2):
                    adj_dic[edge[i]].append(edge[1-i])
                    
            return adj_dic
        
        visited = set()
        adj_lst = adj_lst_mk(edges,n)
        
        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            
            for neighbor in adj_lst[node]:
                if parent != neighbor:
                    if not dfs(neighbor,node):
                        return False
                    
            return True
        
        

        
        return dfs(0,-1) and len(visited) == n
