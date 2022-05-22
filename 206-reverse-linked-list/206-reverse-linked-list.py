# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None 
        
        pre,cur = None,head
        
        while cur != None:
            temp = cur.next
            cur.next = pre
            cur,pre = temp,cur
            
        return pre
    
        
        
    
        
            