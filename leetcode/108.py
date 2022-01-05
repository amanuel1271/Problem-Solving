class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(sortedlst):
            lenn = len(sortedlst)
            if lenn == 0:
                return None
            
            mid = lenn//2
            root = TreeNode(sortedlst[mid],helper(sortedlst[:mid]),helper(sortedlst[mid + 1:]))
            return root
            
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return helper(lst)
