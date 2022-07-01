# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        hashmap,stack = {},[]
        
        while head:
            
            while stack and stack[-1][0] < head.val:
                val,index = stack.pop()
                hashmap[index] = head.val
            
            stack.append((head.val,i))
            i += 1
            head = head.next
            
            
        answer = [0]*i
        
        for idx in hashmap:
            answer[idx] = hashmap[idx]
        
        return  answer
        