# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if not n:
            return None
        
        root = TreeNode(preorder[0])         
        stack = [root] 
        
        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val: 
                node = stack.pop()
             

            if node.val < child.val:
                node.right = child 
            else:
                node.left = child 
                
            stack.append(child)
  
        return root
        
            
        