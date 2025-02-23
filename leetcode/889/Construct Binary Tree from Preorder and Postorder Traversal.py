# solution 1 - traversal, math, index, divide conquer (2025.02.23)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # preorder -> top - down
        # postorder -> bottom - up

        N = len(postorder)  # n 이라고 해버리면, 밑에 n 이랑 겹치니까 N 이라고 설정

        post_val_to_idx = {}  # val -> idx

        for idx, n in enumerate(postorder):
            post_val_to_idx[n] = idx

        # preorder idx : start : i1, end : i2
        # postorder idx : start : j1, end : j2
        def build(i1, i2, j1, j2):
            # print(i1,i2,j1,j2)
            if i1 > i2 or j1 > j2:
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1 + 1]

                until_here = post_val_to_idx[left_val]

                left_size = until_here - j1 + 1

                root.left = build(i1 + 1, i1 + left_size, j1, until_here)
                root.right = build(i1 + left_size + 1, i2, until_here + 1, j2 - 1)

            # print(root)
            return root

        return build(0, N - 1, 0, N - 1)


# solution 2 - traversal, math, index, divide conquer (2025.02.23)
# 사실은 j2 index 는 어차피 preorder 만 봐도 계산할 수 있기 때문에, 필요없다.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # preorder -> top - down
        # postorder -> bottom - up

        N = len(postorder)  # n 이라고 해버리면, 밑에 n 이랑 겹치니까 N 이라고 설정

        post_val_to_idx = {}  # val -> idx

        for idx, n in enumerate(postorder):
            post_val_to_idx[n] = idx

        # preorder idx : start : i1, end : i2
        # postorder idx : start : j1, end : j2
        def build(i1, i2, j1):
            # print(i1,i2,j1,j2)
            if i1 > i2:
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1 + 1]

                until_here = post_val_to_idx[left_val]

                left_size = until_here - j1 + 1

                root.left = build(i1 + 1, i1 + left_size, j1)
                root.right = build(i1 + left_size + 1, i2, until_here + 1)

            # print(root)
            return root

        return build(0, N - 1, 0)




