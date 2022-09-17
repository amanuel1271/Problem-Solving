# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check_palindrome(freq_cnt):
            is_odd = False
            for num in freq_cnt:
                if freq_cnt[num] % 2 == 1:
                    if is_odd:
                        return 0
                    else:
                        is_odd = True
            return 1
                    
        def dfs(node,freq_cnt):
            if node.left is None and node.right is None:
                freq_cnt[node.val] = freq_cnt.get(node.val,0) + 1
                is_pseudo = check_palindrome(freq_cnt)
                freq_cnt[node.val] -= 1
                return is_pseudo
            
            freq_cnt[node.val] = freq_cnt.get(node.val,0) + 1
            left,right = 0,0
            
            if node.left:
                left = dfs(node.left,freq_cnt)
            if node.right:
                right = dfs(node.right,freq_cnt)
                
            freq_cnt[node.val] -= 1
            return left + right
        
        return dfs(root,{})
        