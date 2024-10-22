# solution - my code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        def traversal(node, cur, level):

            if not node:
                return

            l, r = 0, 0
            if node.left:
                l = node.left.val
            if node.right:
                r = node.right.val

            cur.append((l + r, level + 1))
            traversal(node.left, cur, level + 1)
            traversal(node.right, cur, level + 1)

        if not root:
            return -1

        level_sums = [(root.val, 1)]
        traversal(root, level_sums, 1)
        level_sums = sorted(level_sums, key=lambda x: x[1])

        sums_list = [0] * (level_sums[-1][1] - 1)

        if k > len(sums_list):
            return -1

        for ke, va in level_sums:
            if va == len(sums_list) + 1:
                break
            sums_list[va - 1] += ke

        sums_list.sort()
        return sums_list[-k]

# solution 2 - effective solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return -1

        level_sums = defaultdict(int)
        q = deque([(root, 1)])  # (노드,레벨)

        while q:
            node, level = q.popleft()
            level_sums[level] += node.val

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        sums_list = sorted(level_sums.values(), reverse=True)

        if k > len(sums_list):
            return -1

        return sums_list[k - 1]