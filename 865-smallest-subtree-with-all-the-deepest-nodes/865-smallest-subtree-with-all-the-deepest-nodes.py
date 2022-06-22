# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        
        node_to_par = dict()
        val_to_node = dict()
        Q = deque([root])
        last_level_nodes = []
        
        while Q:
            size = len(Q)
            save,last_level_nodes,last_level = last_level_nodes,[],True
            for i in range(size):
                node = Q.popleft()
                val_to_node[node.val] = node
                if node.left:
                    last_level = False
                    node_to_par[node.left] = node
                    Q.append(node.left)
                    last_level_nodes.append(node.left.val)
                if node.right:
                    last_level = False
                    node_to_par[node.right] = node
                    Q.append(node.right)
                    last_level_nodes.append(node.right.val)
                    
            if last_level:
                last_level_nodes = save
                
        last_level_nodes = deque(last_level_nodes)
        size = len(last_level_nodes)
        
        while size > 1:
            visited = set()
            
            for i in range(size):
                val = last_level_nodes.popleft()
                parent_node = node_to_par[val_to_node[val]]
                parent_val = parent_node.val
                visited.add(parent_val)
                
            last_level_nodes = deque(list(visited))
            size = len(last_level_nodes)
            
        #print(last_level_nodes)
        return val_to_node[last_level_nodes.popleft()]
            
                
                
        
            
        