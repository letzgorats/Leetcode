from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.minutes = 0

    def amountOfTime(self, root, start):

        graph = self.convert(root)

        visited = set()
        visited.add(start)

        queue = deque()
        queue.append((start,0))

        while queue:
            node, cnt = queue.popleft()
            if cnt > self.minutes:
                self.minutes = cnt
            
            for n in graph[node]: 
                if n not in visited:
                    visited.add(n)
                    queue.append((n,cnt+1))
    
        return self.minutes

    def convert(self,root):

        graph = defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        
        return graph



        
        
