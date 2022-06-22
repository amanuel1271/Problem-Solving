# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_to_par = dict()
        
        def dfs(node, par = None):
            if node:
                node_to_par[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        
        Q = deque([(target,k)])
        visited = {target}
        ans = []
        
        while Q:
            node,dist = Q.popleft()
            if dist == 0:
                ans.append(node.val)
                continue
            
            for next_node in [node.left,node.right,node_to_par[node]]:
                if next_node and next_node not in visited:
                    visited.add(next_node)
                    Q.append((next_node,dist-1))
        return ans
                

            
            
        