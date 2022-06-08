# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(i,j):
            if i > j:
                return None
            
            subarr = nums[i:j+1]
            
            max_index = subarr.index(max(subarr))
            root = TreeNode(subarr[max_index])
            root.left = helper(i,max_index-1 + i)
            root.right = helper(max_index + 1 + i,j)
            return root
        
        return helper(0,len(nums)-1)