# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.inorderr = []

        def inorder(root):
            
            if not root : return

            inorder(root.left)
            self.inorderr.append(root.val)
            inorder(root.right)

        inorder(root)    
        freq = collections.Counter(self.inorderr)
        maxx = max(freq.values())

        return [x for x in freq if freq[x] == maxx]
