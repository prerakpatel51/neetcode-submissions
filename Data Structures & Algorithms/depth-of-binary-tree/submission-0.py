class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level=0
        queue=deque()
        if not root:
            return 0
        queue.append(root)

        while len(queue)>0:
             level_size=len(queue)
             for i in range(level_size):
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
             level+=1
        return level