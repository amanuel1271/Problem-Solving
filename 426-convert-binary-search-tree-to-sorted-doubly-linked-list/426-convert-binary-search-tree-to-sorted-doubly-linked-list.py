"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def connect(prev,cur):
            prev.right = cur
            cur.left = prev
            
        def helper(node):
            if node:
                helper(node.left)
                connect(self.pre,node)
                self.pre = node
                helper(node.right)
        
        if root:
            dummy = Node(0)
            self.pre = dummy
            helper(root)
            connect(self.pre,dummy.right)
            return dummy.right
        
            
        