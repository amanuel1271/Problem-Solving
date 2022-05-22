# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if  head == None or  head.next == None:
            return head
        
        prev = self.reverseList(head.next)
        head.next.next,head.next = head,None
        return prev
    
        
        
    
        
            