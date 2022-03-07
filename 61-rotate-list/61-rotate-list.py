# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        p = head
        end = None
        while p:
            if not p.next:
                end = p
                
            p = p.next
            length += 1
            
        if not length:
            return head
        
        k %= length
        
        if not k:
            return head
        
        count = length - k - 1
        
        p = head
        for i in range(count):
            p = p.next
            
        start = p.next
        p.next = None
        
        end.next = head
        head = start
        return head
        
            
        
            
        