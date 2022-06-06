# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        index = 1
        start = head
        index_to_node = {}
        
        while start:
            index_to_node[index] = start
            start = start.next
            index += 1
        
        index_to_node[k].val,index_to_node[index-k].val = index_to_node[index-k].val,index_to_node[k].val
        return head