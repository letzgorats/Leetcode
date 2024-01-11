# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def maxAncestorDiff(self, root):
      
        if not root:
            return 0

        # Helper function to calculate the max difference
        def dfs(node, current_max, current_min):
            if not node:
                return current_max - current_min

            current_max = max(current_max, node.val)
            current_min = min(current_min, node.val)

            left_diff = dfs(node.left, current_max, current_min)
            right_diff = dfs(node.right, current_max, current_min)

            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)
