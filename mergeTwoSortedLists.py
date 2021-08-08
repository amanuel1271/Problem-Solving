#  Leetcode easy
#   merge two sorted lists


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addList(self, returnedList : ListNode, appendedList: ListNode):
        starthead = returnedList
        addedList = appendedList
        
        while addedList != None:
            if  not starthead.next or addedList.val <= starthead.next.val:
                nextaddednode = addedList.next
                nexthead = starthead.next
                starthead.next = addedList
                addedList.next = nexthead
                addedList = nextaddednode
                starthead = starthead.next
            else:
                starthead = starthead.next
                
        return returnedList
        
        
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # you have to start from the smallest head node
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val < l2.val:
            return self.addList(l1,l2)   
            
        return self.addList(l2,l1)
        
