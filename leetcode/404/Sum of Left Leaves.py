# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node, attr):

            if not node:
                return 0
            
            if not node.left and not node.right:

                return node.val if attr == 'left' else 0
            
            return dfs(node.left,'left') + dfs(node.right,'right')

        return dfs(root,'root')
