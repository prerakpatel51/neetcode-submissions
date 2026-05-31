# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root_p,root_q):
            if not root_p and not root_q:
                return True
           
            if not root_p or  not root_q:
                return False
            if p.val != q.val:
                return False
            left_match = self.isSameTree(p.left, q.left)
            right_match = self.isSameTree(p.right, q.right)
            return (p.val == q.val) and left_match and right_match
        return dfs(p,q)