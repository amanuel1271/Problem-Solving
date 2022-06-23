class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for person1,person2 in dislikes:
            adj[person1].append(person2)
            adj[person2].append(person1)
            
        color = {}
        def dfs(person):
            for nei in adj[person]:
                if nei in color:
                    if color[nei] == color[person]:
                        return False
                else:
                    color[nei] = 1-color[person]
                    if not dfs(nei):
                        return False
                    
            return True
                    
        
        for person in range(1,n):
            if person not in color:
                color[person] = 0
                if not dfs(person):
                    return False
                
        return True
        