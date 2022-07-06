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
        
        
        def dfs(node):
            if not node:
                return
            if node.val not in to_delete:
                if node.left:
                    save_left = node.left
                    if node.left.val in to_delete:
                        node.left = None
                    dfs(save_left)

                if node.right:
                    save_right = node.right
                    if node.right.val in to_delete:
                        node.right = None
                    dfs(save_right)
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
                
        