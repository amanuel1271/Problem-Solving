class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        sorted1,sorted2 = [],[]
        
        def inorder(node,populate_list):
            if not node:
                return
            inorder(node.left,populate_list)
            populate_list.append(node.val)
            inorder(node.right,populate_list)
            
        inorder(root1,sorted1)
        inorder(root2,sorted2)
        
        len1,len2 = len(sorted1),len(sorted2)
        res = [0] * (len1 + len2)
        
        def merge():
            i,j,k = 0,0,0
            
            while i < len1 and j < len2:
                if sorted1[i] < sorted2[j]:
                    res[k] = sorted1[i]
                    i,k = i+1,k+1
                else:
                    res[k] = sorted2[j]
                    j,k = j+1,k+1
            
            while i < len1:
                res[k] = sorted1[i]
                i,k = i+1,k+1
                
            while j < len2:
                res[k] = sorted2[j]
                j,k = j+1,k+1
            
            
                
        merge()       
        return res
