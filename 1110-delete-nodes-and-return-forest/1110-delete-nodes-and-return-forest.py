# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        
        def break_and_traverse(node,flag):
            next_node = node.left if flag else node.right
            if next_node:
                save = next_node
                if next_node.val in to_delete:
                    if flag:
                        node.left = None
                    else:
                        node.right = None
                dfs(save)
        
        
        def dfs(node):
            if not node:
                return
            if node.val not in to_delete:
                break_and_traverse(node,1)
                break_and_traverse(node,0)
            else:
                save_left = node.left
                save_right = node.right
                node.left,node.right = None,None
                if save_left and save_left.val not in to_delete: ans.append(save_left)
                if save_right and save_right.val not in to_delete: ans.append(save_right)
                dfs(save_left)
                dfs(save_right)
                
        if not root:
            return []
        if root.val not in to_delete: ans.append(root)
        dfs(root)
        return ans
                
        