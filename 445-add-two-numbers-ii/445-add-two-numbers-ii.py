# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1,stack2,res_stack = [],[],[]
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        
        while stack1 or stack2:
            op1,op2 = 0,0
            if stack1:
                op1 = stack1.pop()
            if stack2:
                op2 = stack2.pop()
            
            res_stack.append((op1 + op2 + carry) % 10)
            carry = (op1 + op2 + carry) // 10
            
        if carry > 0:
            res_stack.append(carry)
        
        dummy = ListNode(0)
        ptr = dummy
        
        while res_stack:
            ptr.next = ListNode(res_stack.pop())
            ptr = ptr.next
            
        return dummy.next
    