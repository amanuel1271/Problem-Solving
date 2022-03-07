class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        index_to_values = dict()
        q = [(root, 0)]
        while q:
            print(q[0][0].val)
            curr, index = q.pop(0)
            
            values = index_to_values.get(index, []) + [curr.val]
            index_to_values[index] = values
            
            if curr.left:
                q.append((curr.left, index - 1))
            if curr.right:
                q.append((curr.right, index + 1))
        
        ret = []
        for key in sorted(index_to_values.keys()):
            ret.append(index_to_values[key])
            
        return ret