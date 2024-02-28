from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    depth = 0 
    cnt = 0
    answer = 0

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        #BFS를 사용하여 트리 탐색
        queue = deque([(root,0)]) # (node, depth) 형태
        max_depth = -1
        leftmost_val = None

        while queue:

            node, depth = queue.popleft()

            # 새로운 깊이에 도달하면, 현재 노드를 가장 왼쪽 값으로 업데이트한다.
            if depth > max_depth:
                max_depth = depth
                leftmost_val = node.val
            
            # 자식 노드를 큐에 추가
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))

        return leftmost_val    

