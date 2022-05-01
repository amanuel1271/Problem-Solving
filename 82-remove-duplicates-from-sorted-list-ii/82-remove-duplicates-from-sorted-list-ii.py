# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        f_pointer,s_pointer = dummy_node,dummy_node.next
        
        while f_pointer:
            if s_pointer and s_pointer.next and s_pointer.next.val == s_pointer.val:
                value = s_pointer.val
                while s_pointer and s_pointer.val == value:
                    s_pointer = s_pointer.next

                f_pointer.next = s_pointer
                
            else:
                if s_pointer:
                    s_pointer = s_pointer.next
                f_pointer = f_pointer.next
            
        
    
        return dummy_node.next
        