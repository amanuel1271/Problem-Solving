# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def join(prev,curr):
            if prev == None:
                return curr
            
            attach = prev
            while attach.next:
                attach = attach.next
            attach.next = curr
            return prev
        
        def helper(prev,curr):
            if curr == None:
                return prev
            elif curr.next == None:
                return helper(join(prev,curr),None)
            
            nextt = curr.next.next
            save = curr.next
            curr.next = None
            save.next = curr
            return helper(join(prev,save),nextt)
            
        return helper(None,head)
