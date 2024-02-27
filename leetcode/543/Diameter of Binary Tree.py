# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.answer = 0

        def depth(p):

            if not p : 
                return 0
            left, right = depth(p.left), depth(p.right)
            
            self.answer = max(self.answer, left + right)
            return 1 + max(left, right)
        
        depth(root)
        
        return self.answer
                
        
