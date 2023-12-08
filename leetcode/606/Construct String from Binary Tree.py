
# solution 1) 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def tree2str(self, root):
    
        string = str(root.val)
        
        if root.left:

            string += "(" + self.tree2str(root.left) + ")"
        
        if root.right:

            if not root.left:
                string += "()"
            
            string += "(" + self.tree2str(root.right) + ")"

        return string


# solution 2)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def tree2str(self, root):

        answer = []
        def preorder(node):

            if not node:
                return 

            answer.append("(")
            answer.append(str(node.val))

            if not node.left and node.right:
                answer.append("()")
            preorder(node.left)
            preorder(node.right)
            # answer.append(node.left)
            answer.append(")")


        preorder(root)

        return "".join(answer[1:-1])

    
