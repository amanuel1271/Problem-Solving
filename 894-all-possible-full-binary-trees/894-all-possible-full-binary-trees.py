# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = {1:[TreeNode(0)],3:[TreeNode(0,TreeNode(),TreeNode())]}  
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return self.dic[1]
        elif n % 2 == 0:
            return []
        elif n == 3:
            return self.dic[3]
        output = []
        
        for j in range(1,n):
            if j % 2 == 1 and (n-1-j) % 2 == 1:
                if not j in self.dic:
                    self.dic[j]  = self.allPossibleFBT(j)     
                if not n-1-j in self.dic:
                    self.dic[n-1-j]  = self.allPossibleFBT(n-1-j) 
                    
                for left_tree in self.dic[j]:
                    for right_tree in self.dic[n-1-j]:
                        output.append(TreeNode(0,left_tree,right_tree))  
                        
        self.dic[n] = output
        return output
        