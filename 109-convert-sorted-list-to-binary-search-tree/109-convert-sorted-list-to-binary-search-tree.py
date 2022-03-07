# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(sortedlst):
            lenn = len(sortedlst)
            if lenn == 0:
                return None
            
            mid = lenn//2
            root = TreeNode(sortedlst[mid])
            root.left = helper(sortedlst[:mid])
            root.right = helper(sortedlst[mid + 1:])
            return root
            
            
        
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        return helper(lst)
        