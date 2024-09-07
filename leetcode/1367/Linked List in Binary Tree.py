# TLE code

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(node, prev, curr):

            if not curr:  # 연결 리스트가 끝까지 도달하면 True
                return True
            if not node:  # 트리 노드가 없으면 False
                return False

            if node.val == curr.val:
                prev = curr
                curr = curr.next
                if dfs(node.left, prev, curr) or dfs(node.right, prev, curr):
                    return True  # 왼쪽 또는 오른쪽에서 일치하는 경로 찾기

            return dfs(node.left, dummy, head) or dfs(node.right, dummy, head)  # 새 경로에서 다시 탐색

        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        return dfs(root, prev, curr)


# solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(node, prev, curr):

            if not curr:  # 연결 리스트가 끝까지 도달하면 True
                return True
            if not node:  # 트리 노드가 없으면 False
                return False

            if node.val == curr.val:
                prev = curr
                curr = curr.next
                return dfs(node.left, prev, curr) or dfs(node.right, prev, curr)

            return False

        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        def exploreTree(node):
            if not node:
                return False
            if dfs(node, dummy, head):  # 현재 경로에서 일치하는 부분 경로가 있는지 확인
                return True

            # 자식 노드로 이동하며 탐색 계속
            return exploreTree(node.left) or exploreTree(node.right)

        return exploreTree(root)


