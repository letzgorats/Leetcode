# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def sumNumbers(self, root):

        def dfs(node, currentNumber):

            if not node:
                return 0
            
            currentNumber = currentNumber * 10 + node.val

            if not node.left and not node.right:
                return currentNumber
            
            return dfs(node.left,currentNumber) + dfs(node.right, currentNumber)

        return dfs(root,0)
