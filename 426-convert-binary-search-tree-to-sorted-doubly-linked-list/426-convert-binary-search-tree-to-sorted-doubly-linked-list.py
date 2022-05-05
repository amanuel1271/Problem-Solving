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
        self.pre = None
        def helper(node):
            if node:
                helper(node.left)
                node.left = self.pre
                self.pre.right = node
                self.pre = node
                helper(node.right)
        
        if root:
            dummy = Node(0)
            self.pre = dummy
            helper(root)
            self.pre.right = dummy.right
            dummy.right.left = self.pre
            return dummy.right
        
            
        