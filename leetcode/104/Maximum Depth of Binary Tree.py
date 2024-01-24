# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.depth = 1
        self.tmp = 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            
            return 0

        if root.left or root.right:
            self.tmp += 1
            self.maxDepth(root.left)
            self.maxDepth(root.right)
            self.tmp -= 1
       
        self.depth = max(self.depth,self.tmp)

        return self.depth

        
