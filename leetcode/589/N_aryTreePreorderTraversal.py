"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        stack = [root.val]

        for node in root.children:
            stack.extend(self.preorder(node))
        
        return stack
      
      
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        # iterative
        if not root :
            return []
        
        stack = [root]
        answer = []

        while stack:
            cur_node = stack.pop()
            answer.append(cur_node.val)
            stack.extend(cur_node.children[::-1])
        
        return answer
