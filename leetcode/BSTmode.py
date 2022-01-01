# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,dic):
            if not root:
                return
            
            if root.val in dic:
                dic[root.val] += 1
            else:
                dic[root.val] = 1
            
            helper(root.left,dic)
            helper(root.right,dic)
        
        
        
        lookup_dict,res = {},[]
        helper(root,lookup_dict)
        
        maxx = max(lookup_dict.values())
        return [key for key in lookup_dict if lookup_dict[key] == maxx]
