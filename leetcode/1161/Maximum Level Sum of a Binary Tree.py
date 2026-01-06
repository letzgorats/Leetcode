# solution 1 - (tree,bfs) - (31ms) - (2026.01.06)
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque([root])
        max_level = 1
        max_sum = float('-inf')
        level = 1

        while q:
            level_sum = 0
            next_level = []

            for node in q:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            q = next_level
            level += 1

        return max_level

# solution 2 - (dfs,defaultdict) - (49ms) - (2026.01.06)
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(int)

        def sum_vals(node, depth):
            if node:
                levels[depth] += node.val
                sum_vals(node.left, depth + 1)
                sum_vals(node.right, depth + 1)

        sum_vals(root, 1)

        return max(levels, key=levels.get)