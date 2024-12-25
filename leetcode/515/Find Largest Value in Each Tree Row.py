# solution 1 - bfs
from collections import deque
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

# solution 2 - dfs

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        level_per_val = defaultdict(list)

        def dfs(node, level):

            if not node:
                return
            level_per_val[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 1)
        answer = []
        for k, tmp in level_per_val.items():
            answer.append(max(tmp))

        return answer
