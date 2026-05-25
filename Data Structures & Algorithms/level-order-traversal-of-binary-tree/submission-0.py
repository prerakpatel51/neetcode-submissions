# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        res=[]

        if not root:
            return []
        queue.append(root)
        while len(queue)>0:
            temp_res=[]
            for i in range(len(queue)):
                curr=queue.popleft()

                temp_res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(temp_res)
        return res