class Solution(object):
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False

        targetSum = targetSum - root.val

        if root.left is None and root.right is None:
            return targetSum == 0
        
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)


# second-try 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        def dfs(root,cost):
        
            if not root:
                return False

            cost += root.val

            
            # only leaf node
            if (not root.left and not root.right):
                return cost == targetSum

            return dfs(root.left,cost) or dfs(root.right,cost)


        return dfs(root,0)
