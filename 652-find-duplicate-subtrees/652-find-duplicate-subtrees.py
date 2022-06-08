# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        post_order_dic = {}
        res = []
        res_set = set()
        
        def dfs(node):
            if not node:
                return ''
            
            post_order = dfs(node.left) + ' ' + dfs(node.right) + ' ' + str(node.val)
            
            if post_order in post_order_dic and post_order not in res_set:
                res.append(post_order_dic[post_order])
                res_set.add(post_order)
            elif post_order not in post_order_dic:
                post_order_dic[post_order] = node 
            return post_order
        
        dfs(root)
        return res
            
            
        