# BFS solution - my solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        queue = deque([(root,1)])
     
        while queue:

            node, depth = queue.popleft()
            # print(node,depth)
            if node.left:
                queue.append((node.left, depth+1))  
            
            if node.right:
                queue.append((node.right, depth+1))

            elif not node.left and not node.right:
                return depth

        return depth 


# DFS solution
def minDepth1(self, root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
