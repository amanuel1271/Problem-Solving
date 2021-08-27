############### Has some minor bug that I couldnt figure out , but the idea is ok

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.dic = {}
        
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            self.dic[1] = [TreeNode(0)]
            return self.dic[1]
        elif n % 2 == 0:
            return []
        elif n == 3:
            self.dic[3] = [TreeNode(0,TreeNode(),TreeNode())]
            return self.dic[3]
        output = []
        
        for j in range(1,((n-1)//2) + 1):
            if j%2 == 1 and (n-1-j)%2 == 1:
                
                if not j in self.dic:
                    self.dic[j]  = self.allPossibleFBT(j)     
                if not n-1-j in self.dic:
                    self.dic[n-1-j]  = self.allPossibleFBT(n-1-j)  
                for tree_1 in self.dic[j]:
                    for tree_2 in self.dic[n-1-j]:
                        x1 = TreeNode(0,tree_1,tree_2)
                        if not x1 in output:
                            output.append(x1)
                        x2 = TreeNode(0,tree_2,tree_1)
                        if not x2 in output and not tree_1 is tree_2:
                            output.append(x2)
                            
        self.dic[n] = output
        return output
