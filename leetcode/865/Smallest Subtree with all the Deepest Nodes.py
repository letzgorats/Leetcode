# solution 1 - (tree,dfs) - (0ms) - (2026.01.09)
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Return (LCA=lowest common ancestor, height)
        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height == right_height:
                return node, 1 + left_height
            elif left_height > right_height:
                return left_node, left_height + 1
            else:
                return right_node, right_height + 1

        node, _ = dfs(root)

        return node

# solution 2 - (tree,dfs) - (0ms) - (2026.01.09)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Return (LCA=lowest common ancestor, depth)
        def dfs(node, depth):
            if not node:
                return (None, depth + 1)

            left_node, left_depth = dfs(node.left, depth + 1)
            right_node, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left_node, left_depth
            elif left_depth < right_depth:
                return right_node, right_depth
            return node, left_depth

        node, _ = dfs(root, 0)

        return node