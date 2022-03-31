"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors_of_q = set()
        def descendant_of_one(ancestor,descendant):
            par = descendant.parent
            while par:
                if descendant is q:
                    ancestors_of_q.add(par)
                    
                if descendant is p and par in ancestors_of_q:
                    return par
                
                if par is ancestor:
                    return ancestor
                par = par.parent
                
            return None
        
        return p if descendant_of_one(p,q) else descendant_of_one(q,p)

        
        
        