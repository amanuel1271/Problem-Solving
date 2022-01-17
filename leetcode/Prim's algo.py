'''
Inefficient 
Prim's algorithm implementation (Time limit exceeded)
'''

class Solution:
    def adjList(self,points,n):
        adj = {}
        
        for i in range(n):
            adj[i] = []
            
        for i in range(n):
            for j in range(i+1,n):
                cost = abs(points[i][0]- points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append((j,cost))
                adj[j].append((i,cost))
        
        return adj
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjacency = self.adjList(points,n)
        
        visited,unvisited = set(),set()
        for j in range(n):
            unvisited.add(j)
        
        visited.add(unvisited.pop())
        final_cost = 0
        prev_min = (0,math.inf)

            
        while len(visited) != n:
            min_tuple = (0,math.inf) # contains the edge to be added to the visited set
            
            for items in visited:
                
                for edge,cost in adjacency[items]:
                    if edge in visited:
                        continue
                    if cost < min_tuple[1]:
                        min_tuple = (edge,cost)
            
    
                
            visited.add(min_tuple[0])
            final_cost += min_tuple[1]
            unvisited.remove(min_tuple[0])
            
        return final_cost
