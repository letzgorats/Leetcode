# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.answer = []

        def traversal(node):
            if not node:
                return

            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)

            self.answer.append(node.val)

        traversal(root)
        return self.answer