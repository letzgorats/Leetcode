# solution 1 - helper function,dfs,reduce - (0ms) - (2025.04.04)
from functools import reduce


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        max_depth = 0
        node_path = []

        def dfs(node, depth):
            nonlocal max_depth

            if not node.left and not node.right:
                if max_depth <= depth:
                    if max_depth < depth:
                        node_path.clear()  # 더 깊은 노드가 나오면 이전 건 무시
                    max_depth = depth
                    node_path.append(node)
                return

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)

        # print(node_path)
        # LCA 를 찾는 전형적인 재귀 알고리즘
        answer = TreeNode()

        def find_lca(node, p, q):  # root, left, right 로 이해하면 된다.

            if not node or node == p or node == q:
                return node

            # left 는 왼쪽 서브트리에서 p 또는 q 를 찾았을 경우 그 노드를 반환
            # right 는 오른쪽 서브트리에서 p 또는 q 를 찾았을 경우 그 노드를 반환
            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)

            # 둘 다 찾았다면?
            # 둘 다 찾았다는 것은 p와 q가 서로 다른 서브트리에 있다는 뜻이고,
            # 따라서 지금 이 node 가 처음으로 두 노드를 동시에 포함하는 공통 조상, 즉 LCA 가 된다.
            if left and right:
                return node

            return left or right  # 존재하는 쪽으로 위로 계속 반환하는 역할

        # reduce는 find_lca(node,a,b) -> 그 결과를 c랑 또 비교하는 식으로 점점 공통 조상을 축소해나간다.
        answer = reduce(lambda x, y: find_lca(root, x, y), node_path)
        '''
        reduce(function,iterable)

        -> function 은 두 개의 인자를 받아서 결과를 리턴한다.
        -> iterable은 리스트나 튜플처럼 여러 값을 가진 시퀀스 데이터
        -> reduce 는 "처음 두 개의 값"으로 "function(a,b)"를 실행하고, 그 결과를 가지고 다음 값과 또 실행한다.
            즉, 계속 이 작업을 반복해서 최종 하나의 값으로 줄여나가는 것이다.

        (ex) nums = [1,2,3,4] 
            result = reduce(lambda x,y : x + y, nums)
            print(result) # 10

            step 1 : x=1,y=2 -> x+y = 3
            step 2 : x=3,y=3 -> x+y = 6
            step 3:  x=6,y=4 -> x+y = 10

        따라서, reduce(lambda x,y : find_lca(root,x,y), node_path) 라고 하면,
        만약 node_path = [node7, node4, node9] 라고 하면

            step 1 : find_lca(root,node7,node4) -> 공통 조상 A 반환(node2)
            step 2 : find_lca(root,A,node9) -> 공통 조상 B 반환
            step 3:  결국 B 가 최종 LCA
        '''
        return answer


# solution 2 - dfs - (0ms) - (2025.04.04)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        def dfs(node, depth):

            if not node.left and not node.right:
                return node, depth

            left, l_depth = dfs(node.left, depth + 1) if node.left else (node, depth)
            right, r_depth = dfs(node.right, depth + 1) if node.right else (node, depth)

            if l_depth == r_depth:
                return node, l_depth

            return (left, l_depth) if l_depth > r_depth else (right, r_depth)

        lca, _ = dfs(root, 0)
        return lca