# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.curSum = 0

        def dfs(node):

            if node != None:

                dfs(node.right)
                self.curSum += node.val
                node.val = self.curSum
                dfs(node.left)

                return node

        return dfs(root)
