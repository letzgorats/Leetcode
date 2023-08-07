class Solution(object):
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False

        targetSum = targetSum - root.val

        if root.left is None and root.right is None:
            return targetSum == 0
        
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
