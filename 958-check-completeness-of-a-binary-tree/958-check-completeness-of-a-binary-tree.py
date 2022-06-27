# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        full_level = True
        
        while queue:
            size = len(queue)
            if size != 2**level:
                full_level = False
                
            is_empty = False
            num_of_children = 0
                
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    if is_empty:
                        return False
                    queue.append(node.left)
                    num_of_children += 1
                else:
                    is_empty = True
                if node.right:
                    if is_empty:
                        return False
                    queue.append(node.right)
                    num_of_children += 1
                else:
                    is_empty = True
                    
            level += 1
                    
            if not full_level and num_of_children > 0:
                return False
            
        return True
                
            
        