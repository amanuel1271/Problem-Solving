# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        big_dummy = ListNode(-101)
        greater = big_dummy
        
        small_dummy = ListNode(-101)
        small_dummy.next = head
        least = small_dummy
        
        while least.next:
            if least.next.val >= x:
                greater.next = ListNode(least.next.val)
                greater = greater.next
                least.next = least.next.next
            else:
                least = least.next
                
        least.next = big_dummy.next
        return small_dummy.next
        
                
            
            
        
        
        