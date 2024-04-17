# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        answer = []
        if not root:
            return ""

        def dfs(node,cur):
            
            if not node.left and not node.right:
                cur += str(chr(node.val+97))
                answer.append(cur[::-1])
                return
            
            if node.left:
                dfs(node.left,cur + str(chr(node.val+97)))
            if node.right:
                dfs(node.right,cur + str(chr(node.val+97)))
    
        if not root.left and not root.right:
            return str(chr(root.val+97))
        if root.left:
            dfs(root.left,str(chr(root.val+97)))
        if root.right:
            dfs(root.right,str(chr(root.val+97)))
        

        answer = sorted(answer)
        # print(answer)

        return answer[0]
