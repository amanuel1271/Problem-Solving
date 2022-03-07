# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''':type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode '''
                
        p = l1
        q = l2
        prev_sum = None
        sum_lst = None
        carry = 0
        while p or q:
            a = 0 if not p else p.val
            b = 0 if not q else q.val
            sum = a + b + carry
            curr_sum = ListNode(sum % 10)
            if not sum_lst:
                sum_lst = prev_sum = curr_sum
            else:
                prev_sum.next = curr_sum
                prev_sum = curr_sum
                
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            if p:
                p = p.next
            if q:
                q = q.next
            
        if carry:
            curr_sum.next = ListNode(1)
        return sum_lst
        