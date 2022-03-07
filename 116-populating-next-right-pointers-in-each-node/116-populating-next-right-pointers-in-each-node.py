"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = []
        queue.append(root)
        
        while queue:
            len_ = len(queue)
            
            for i in range(len_):
                froot = queue.pop(0)

                if i < len_ - 1:
                    froot.next = queue[0]
                    
                if froot.left:
                    queue.append(froot.left)
                    queue.append(froot.right)
                    
    
        
        return root
                
                    
            
            
        