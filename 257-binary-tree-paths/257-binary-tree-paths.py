# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root):
            if root and not root.left and not root.right:
                return [str(root.val)]
            
            left_lst,right_lst = [],[]
            
            if root.left:
                left_lst = helper(root.left)
            if root.right:
                right_lst = helper(root.right)
            
            for i in range(len(left_lst)):
                left_lst[i] = (str(root.val) + '->') + left_lst[i]
                
            for i in range(len(right_lst)):
                right_lst[i] = (str(root.val) + '->') + right_lst[i]
                
            return left_lst + right_lst
        
        return helper(root)
            
            
                