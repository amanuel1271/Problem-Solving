
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output  = []
        
        if not root:
            return output
        
        output.append([root.val])
        store_parent_node = [root]
        
        while any(store_parent_node):
            inner_list = []
            hold_roots = []
            for root in store_parent_node:
                if root:
                    if root.left:
                        inner_list.append(root.left.val)
                        hold_roots.append(root.left)
                    if root.right:
                        inner_list.append(root.right.val)
                        hold_roots.append(root.right)

            if inner_list:
                output.append(inner_list)
            
            store_parent_node = hold_roots
        
                
            
        return output
                    
                    
            
        
        
        
