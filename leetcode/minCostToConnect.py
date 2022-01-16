class Solution:
    def __init__(self):
        self.array = []
        
    def union(self,x,y):
        headx,heady = self.find(x),self.find(y)
        if headx != heady:
            for i in range(len(self.array)):
                if self.find(i) == heady:
                    self.array[i] = headx
                    
    def find(self,index):
        return self.array[index] ##returns the head of the connected vertices
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge_cost = []
        n = len(points)
        self.array = [i for i in range(n)]
        
        for i in range(n):
            for j in range(i + 1,n):
                dist = abs(points[i][0]- points[j][0]) + abs(points[i][1]-points[j][1])
                edge_cost.append((i,j,dist))
            
        edge_cost.sort(key = lambda x:x[2]) # sorted by cost 
        cost_count,edge_count = 0,0
        
        for edge1,edge2,cost in edge_cost:
            if edge_count == n-1:
                break
                
            head1,head2 = self.find(edge1),self.find(edge2)
            
            if head1 != head2: # if no cycle
                self.union(edge1,edge2)
                edge_count += 1
                cost_count += cost
                
        return cost_count
