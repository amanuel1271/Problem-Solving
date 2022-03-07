# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = n
        p = head
        while count and p:
            p = p.next
            count -= 1
       
        q = head
        if not p:
            return head.next
        
        while p:
            q_prev = q
            p = p.next
            q = q.next
            
        q_prev.next = q.next
        return head
        