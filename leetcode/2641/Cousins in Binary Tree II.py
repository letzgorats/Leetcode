# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        node_sum = []
        q = deque([(root, 0)])
        while q:

            node, level = q.popleft()
            node_sum.append((node.val, level))
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        level_sum = [0] * (node_sum[-1][-1] + 1)
        for val, level in node_sum:
            level_sum[level] += val

        q = deque([(root, root.val)])  # (node,child_sum)
        level = 0
        while q:
            for i in range(len(q)):
                node, val = q.popleft()
                node.val = level_sum[level] - val

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val

                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))

            level += 1

        return root