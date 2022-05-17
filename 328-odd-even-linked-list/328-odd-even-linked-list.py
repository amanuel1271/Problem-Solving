# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        evenhead = ListNode(0,head.next) if head else ListNode(0,None)
        even = evenhead.next
        
        while even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
                even.next = odd.next
                even = even.next
            else:
                even.next = None
                even = even.next
                
                
        if odd:
            odd.next = evenhead.next
            
        return head
                
            
        
        
        
        
        