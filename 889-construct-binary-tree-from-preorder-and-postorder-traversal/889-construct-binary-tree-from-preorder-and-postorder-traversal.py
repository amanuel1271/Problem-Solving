# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        val_to_idx = {x:i for i,x in enumerate(preorder)}
        
        def construct(i1,i2,j1,j2):
            if i1 > i2:
                return None
            root = TreeNode(preorder[i1])
            if j1 == j2:
                return root
            
            idx = val_to_idx[postorder[j2-1]] - val_to_idx[preorder[i1]]
            root.left = construct(i1+1,i1+idx-1,j1,j1+idx-2)
            root.right = construct(i1+idx,i2,j1+idx-1,j2-1)
            return root
        
        return construct(0,len(preorder)-1,0,len(postorder)-1)

    
        