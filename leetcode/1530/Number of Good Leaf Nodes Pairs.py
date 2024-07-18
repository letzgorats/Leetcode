# solution 1 -  O(n×(logn) ^2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        self.answer = 0
        def dfs(node):

            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        self.answer += 1

            all_dist = left_dist + right_dist
            return [d + 1 for d in all_dist]

        dfs(root)
        return self.answer

# solution 2 - O(n*distance^2)
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        self.answer = 0

        def dfs(node):

            if not node:
                return defaultdict(int)

            if not node.left and not node.right:
                count = defaultdict(int)
                count[1] = 1
                return count

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        self.answer += left_dist[d1] * right_dist[d2]

            all_dist = defaultdict(int)
            for d in left_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] = left_dist[d]
            for d in right_dist:
                if d + 1 <= distance:
                    all_dist[d + 1] += right_dist[d]

            return all_dist

        dfs(root)
        return self.answer

# solution 3 - bfs soultion, O(n^2)
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        adj = defaultdict(list)
        leaf_set = set()

        def build_graph(node):
            if not node:
                return

            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
            if not node.left and not node.right:
                leaf_set.add(node)

            build_graph(node.left)
            build_graph(node.right)

        def bfs(node):
            visited = set([node])
            q = deque([(node, 0)])

            while q:

                curr, dist = q.popleft()

                if curr != node and curr in leaf_set and dist <= distance:
                    self.answer += 1

                for nei in adj[curr]:
                    if nei not in visited and dist + 1 <= distance:
                        q.append((nei, dist + 1))
                        visited.add(nei)

        build_graph(root)
        self.answer = 0
        for node in leaf_set:
            bfs(node)

        return self.answer // 2
