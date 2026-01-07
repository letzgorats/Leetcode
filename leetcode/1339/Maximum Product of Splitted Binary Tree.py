# solution 1 - (dfs,bfs,tree) - (47ms) - (2026.01.07)
# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 1e9 + 7

        def dfs(node):
            if not node:
                return 0

            node.val += dfs(node.left) + dfs(node.right)
            return node.val

        # 전체 node value 구하기
        total = dfs(root)
        print(total)

        ans = 0
        q = deque([root])

        while q:

            node = q.popleft()
            if not node:
                continue

            current_product = (total - node.val) * node.val
            ans = max(ans, current_product)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return int(ans % MOD)