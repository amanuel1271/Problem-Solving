# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(numlist):
            
            lenn = len(numlist)
            if lenn == 0:
                return None
            elif lenn == 1:
                return TreeNode(numlist[0],None,None)
            elif lenn == 2:
                return TreeNode(numlist[1],TreeNode(numlist[0]),None)
            
            mid = lenn // 2
            
            return TreeNode(numlist[mid],helper(numlist[:mid]),helper(numlist[mid+1:]))
            
            
        
        nums.sort()
        return helper(nums)
        
