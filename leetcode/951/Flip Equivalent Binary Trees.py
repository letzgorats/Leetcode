# solution 1 - recursive(dfs)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traversal(node1, node2):

            # 둘 다 None 인 경우 - 같음
            if not node1 and not node2:
                return True

            # 한쪽만 Nonde인 경우 - 다름
            if not node1 or not node2:
                return False

            # 현대 노드의 값이 다르면 바로 False
            if node1.val != node2.val:
                return False

            # 자식들을 flip 하지 않은 상태에서 비교 (left-left, right-right)
            no_flip = traversal(node1.left, node2.left) and traversal(node1.right, node2.right)

            # 자식들을 flip 한 상테에서 비교 (left-right,right-left)
            flip = traversal(node1.left, node2.right) and traversal(node1.right, node2.left)

            # 두 가지 경우 중 하나라도 True면 flip equivalent
            return no_flip or flip

        return traversal(root1, root2)