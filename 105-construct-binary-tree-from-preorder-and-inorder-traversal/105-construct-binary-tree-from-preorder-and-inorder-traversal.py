# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {x:i for i,x in enumerate(inorder)}
        
        def construct(i1,i2,j1,j2):
            if i1 > i2 or j1 > j2:
                return None
            
            root = TreeNode(preorder[i1])
            mid = val_to_index[preorder[i1]] - val_to_index[inorder[j1]]
            root.left = construct(i1 + 1,i1+mid,j1,j1+mid-1)
            root.right = construct(i1+mid+1,i2,j1+mid+1,j2)
            return root
        
        return construct(0,len(preorder)-1,0,len(inorder)-1)
