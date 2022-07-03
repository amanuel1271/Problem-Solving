# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        ans = [[-1]*n for _ in range(m)]
        
        
        x,y = 0,0
        ori = 'E'
        ori_to_next_pos = {'E': (0,1),'W': (0,-1),'N': (-1,0),'S': (1,0)}
        dir_ = {'E':'S','S':'W','W':'N','N':'E'}
        
        while head:
            ans[x][y] = head.val
            nxt_p = ori_to_next_pos[ori]
            next_x,next_y = x + nxt_p[0],y + nxt_p[1]
            
            if 0 <= next_x < m and 0 <= next_y < n and ans[next_x][next_y] == -1:
                x,y = next_x,next_y
            else:
                ori = dir_[ori]
                nxt_p = ori_to_next_pos[ori]
                x,y = x + nxt_p[0],y + nxt_p[1]
                
            head = head.next
            
        return ans
        
        
        