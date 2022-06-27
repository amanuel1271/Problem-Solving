# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        full_level = True
        is_empty = False
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    if is_empty:
                        return False
                    queue.append(node.left)
                else:
                    is_empty = True
                if node.right:
                    if is_empty:
                        return False
                    queue.append(node.right)
                else:
                    is_empty = True
                    
            
        return True
                
            
        