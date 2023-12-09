# solution 1)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# solution 2)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.answer = []
        def inorder(root):
            if not root :

                return

            inorder(root.left)
            self.answer.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return self.answer
