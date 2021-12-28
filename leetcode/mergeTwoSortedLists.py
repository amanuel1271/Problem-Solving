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
    
    
    
 /**** Recursive approach ****/
    
 class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(added,merged):
            if added == None:
                return merged
            elif merged.next == None:
                merged.next = added
                return merged  
            
            added_head = added
            enter = False
            while added_head.val <= merged.next.val:
                enter = True
                if added_head.next == None or added_head.next.val > merged.next.val:
                    break
                added_head = added_head.next
                
            if enter:
                save_nexta = added_head.next
                added_head.next = merged.next
                merged.next = added
            else:
                save_nexta = added_head
                
            helper(save_nexta,merged.next)
            return merged
        
        if list1 == None or (list2 != None and list2.val <= list1.val):
            return helper(list1,list2)
        return helper(list2,list1)
        
