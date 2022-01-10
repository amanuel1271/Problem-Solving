class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        def helper(start,visited,adj_lst):
            if [start,end]  in edges or [end,start] in edges:
                return True
            elif start == end:
                return True
            for edge in  adj_lst[start]:
                if edge not in visited:
                    visited.add(edge)
                    if helper(edge,visited,adj_lst):
                        return True
            return False
        
        def adjacent_list_mk(edges,n):
            adj_dic = {}
            for i in range(n):
                adj_dic[i] = []
            for edge in edges:
                for i in range(2):
                    adj_dic[edge[i]].append(edge[1-i])   
            return adj_dic
                    
            
        
        if start > n:
            return False
        elif start == end:
            return True
        
        visited = {start}
        return helper(start,visited,adjacent_list_mk(edges,n))
        
