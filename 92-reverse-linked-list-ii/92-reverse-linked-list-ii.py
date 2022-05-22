# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        p = dummy = ListNode(0,head)
        for _ in range(left - 1):
            p = p.next
            
        cur = p.next
        pre = None
        for _ in range(right - left + 1):
            cur.next, pre, cur = pre, cur, cur.next
            
        p.next.next,p.next = cur,pre
        return dummy.next
        