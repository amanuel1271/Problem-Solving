# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        visited,stack,inorder = set(),deque(),[]
        
        visited.add(root)
        stack.append(root)
        
        while stack:
            curoot = stack[-1]
            if curoot.left and curoot.left not in visited:
                visited.add(curoot.left)
                stack.append(curoot.left)
            elif curoot.right and curoot.right not in visited:
                inorder.append(curoot.val)
                stack.append(curoot.right)
                visited.add(curoot.right)
            elif curoot.right in visited:
                stack.pop()
            else:
                inorder.append(curoot.val)
                stack.pop()
                
        
        return inorder
                
                

                
                
            
        
        
        
        
        
        