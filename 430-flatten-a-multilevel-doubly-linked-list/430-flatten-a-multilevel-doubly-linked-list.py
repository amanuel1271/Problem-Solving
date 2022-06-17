"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def flatten_child(head):
            ptr,tail = head,head
            while ptr:
                tail = ptr
                if ptr.child:
                    front,back = flatten_child(ptr.child)
                    ptr.next,back.next = front,ptr.next
                    tail = back
                    ptr.next.prev = ptr
                    if back.next:
                        back.next.prev = back
                    ptr.child = None
                    ptr = back.next
                else:
                    ptr = ptr.next
                    
            return head,tail
        
        dummy = Node(10,None,None,head)
        flatten_child(dummy)
        if dummy.next:
            dummy.next.prev = None
        return dummy.next
        
        
        