# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fpointer,spointer = dummy,dummy.next
        
        while fpointer:
            if spointer and spointer.next and spointer.next.val == spointer.val:
                value = spointer.val
                while spointer and spointer.val == value:
                    spointer = spointer.next

                fpointer.next = spointer
                
            else:
                if spointer:
                    spointer = spointer.next
                fpointer = fpointer.next
            
        
    
        return dummy.next
        