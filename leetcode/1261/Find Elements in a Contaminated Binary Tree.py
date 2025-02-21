# solution 1 - dfs, traversal - 408ms - (2025.02.21)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.answer = []

        def traversal(node, val):

            if not node:
                return

            # 해당 노드가 None 이 아니면
            node.val = val  # 노드의 val 을 인자 val 로 할당
            self.answer.append(val)  # self.answer에 노드 val 포함

            if node.left:  # 좌측에 노드가 있으면
                traversal(node.left, val * 2 + 1)  # 좌측 노드로 이동, 값*2 + 1

            if node.right:  # 우측에 노드가 있으면
                traversal(node.right, val * 2 + 2)  # 우측 노드로 이동, 값*2 + 2

        traversal(root, root.val)
        # print(root)
        # print(self.answer)

    def find(self, target: int) -> bool:

        if target in self.answer:
            return True
        return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# solution 2 - dfs, traversal, set - 5ms (2025.02.21)
# set 을 사용하는것으로만으로 O(n) 에서 O(1) 로 줄일 수 있음.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.answer = set()

        def traversal(node, val):

            if not node:
                return

            # 해당 노드가 None 이 아니면
            node.val = val  # 노드의 val 을 인자 val 로 할당
            self.answer.add(val)  # self.answer에 노드 val 포함

            if node.left:  # 좌측에 노드가 있으면
                traversal(node.left, val * 2 + 1)  # 좌측 노드로 이동, 값*2 + 1

            if node.right:  # 우측에 노드가 있으면
                traversal(node.right, val * 2 + 2)  # 우측 노드로 이동, 값*2 + 2

        traversal(root, root.val)
        # print(root)
        # print(self.answer)

    def find(self, target: int) -> bool:

        return target in self.answer

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)