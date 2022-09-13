class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return (False,0)
            visited.add(node)
            second = 0
            for child in adj[node]:
                has_some_apple,child_value = dfs(child)
                if has_some_apple:
                    second += child_value + 2
                
            if (second == 0 and hasApple[node]) or second > 0:
                return (True,second)
            return (False,0)
        
        return dfs(0)[1]
                
        