from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        queue = deque([(root,0)]) # (node, depth)의 형태  

        while queue:

            pre_val = None
            for _ in range(len(queue)):
                node, depth = queue.popleft()
            
                # 깊이가 짝수라면
                if depth % 2 == 0 :
                    if node.val % 2 == 0 or (pre_val is not None and node.val <= pre_val):
                        return False

                # 깊이가 홀수라면
                else:
                    if node.val % 2 == 1 or (pre_val is not None and node.val >= pre_val):
                        return False
            
                pre_val = node.val


                if node.left:
                    queue.append((node.left, depth+1))

                if node.right:
                    queue.append((node.right,depth+1))

        return True
