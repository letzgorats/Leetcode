# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.answer = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        if not root:
            return

        if low <= root.val <= high:     
            self.answer += root.val
        

        self.rangeSumBST(root.left,low,high)        
        self.rangeSumBST(root.right,low,high)        

        return self.answer


        
