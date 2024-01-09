# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):

        self.tree = []     
    
    def traversal(self,node):

        if not node:
            return 

        if node.left is None and node.right is None:
            self.tree.append(node.val)
            return self.tree
        
        self.traversal(node.left)
        self.traversal(node.right)

        return self.tree


    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        tree1 = self.traversal(root1)
        self.tree = []
        tree2 = self.traversal(root2)

        # print(tree1)
        # print(tree2)

        return tree1 == tree2

