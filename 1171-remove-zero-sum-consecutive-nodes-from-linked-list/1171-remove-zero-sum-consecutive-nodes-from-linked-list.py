# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prefixSumToNode = {0: dummy}
        sum_ = 0
        
        def deleteSums(ptr,cur_sum,head):
            while ptr != head.next:
                cur_sum += ptr.val
                if cur_sum in prefixSumToNode and ptr == prefixSumToNode[cur_sum]:
                    del prefixSumToNode[cur_sum]
                ptr = ptr.next
        
        
        while head:
            sum_ += head.val
            
            if sum_ in prefixSumToNode:
                node =  prefixSumToNode[sum_]
                deleteSums(node.next,sum_,head)
                node.next = head.next
                head = node.next
            else:
                prefixSumToNode[sum_] = head
                head = head.next
                
        return dummy.next
            
                
        
        
        