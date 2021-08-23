class Solution:
    def __init__(self):
        self.elem = []
    def append(self,root):
        if root == None:
            return
        
        self.elem.append(root.val)
        self.append(root.right)
        self.append(root.left)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.append(root)
        return sorted(self.elem)[k - 1]
