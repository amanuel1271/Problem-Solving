# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        index_map = {nums[i]:i for i in range(len(nums))}
        
        def helper(i,j):
            if i > j:
                return None
            
            
            max_index = index_map[(max(nums[i:j+1]))]
            root = TreeNode(nums[max_index])
            root.left = helper(i,max_index-1)
            root.right = helper(max_index + 1,j)
            return root
        
        return helper(0,len(nums)-1)