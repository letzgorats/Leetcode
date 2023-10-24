# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        answer = []

        if not root:
            return answer
        
        queue = deque([root])

        while queue:
            level_max = float('-inf')
            level = len(queue)
            for i in range(level):
                temp = queue.popleft()
                level_max = max(level_max,temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            answer.append(level_max)

        return answer
