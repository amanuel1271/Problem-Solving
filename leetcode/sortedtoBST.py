# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(numlist):
            
            len_ = len(numlist)
            if len_ == 0:
                return None
            elif len_ == 1:
                return TreeNode(numlist[0],None,None)
            elif len_ == 2:
                return TreeNode(numlist[1],TreeNode(numlist[0]),None)
            
            mid = len_//2
            
            return TreeNode(numlist[mid],helper(numlist[:mid]),helper(numlist[mid+1:]))
            
            
        
        nums.sort()
        return helper(nums)
        
