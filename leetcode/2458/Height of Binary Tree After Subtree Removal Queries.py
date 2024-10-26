# solution 1 - dfs x 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # 노드가 제거되었을 때 최대 높이를 기록할 딕셔너리
        heights_after_removal = defaultdict(int)

        # 트리의 높이를 계산하는 재귀 함수
        def calculate_height(node, depth, current_max):
            if not node:
                return current_max

            # 현재 노드의 값을 업데이트
            heights_after_removal[node.val] = max(heights_after_removal[node.val], current_max)

            # 좌우 자식을 바꿔서 탐색
            node.left, node.right = node.right, node.left

            # 왼쪽과 오른쪽 순서로 재귀 호출
            return calculate_height(node.right, depth + 1,
                                    calculate_height(node.left, depth + 1, max(current_max, depth)))

        # 트리를 두 번 순회해서 필요한 정보를 계산
        calculate_height(root, 0, 0)
        calculate_height(root, 0, 0)

        # 쿼리에 해당하는 높이 값을 반환
        return [heights_after_removal[q] for q in queries]


# solution 2 - precompute + dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        depths = {}
        heights = {}

        # Step 1: Compute heights and depths using DFS
        def compute_heights(node, depth):
            if not node:
                return -1

            depths[node.val] = depth
            left_height = compute_heights(node.left, depth + 1)
            right_height = compute_heights(node.right, depth + 1)

            heights[node.val] = 1 + max(left_height, right_height)

            return heights[node.val]

        compute_heights(root, 0)

        # Step 2: Precompute the maximum heights for each level excluding subtrees
        max_height_without_subtree = {}
        level_max_height = {}

        def update_level_heights(node):
            if not node:
                return
            depth = depths[node.val]
            if depth not in level_max_height:
                level_max_height[depth] = []
            level_max_height[depth].append(heights[node.val])
            update_level_heights(node.left)
            update_level_heights(node.right)

        update_level_heights(root)

        # Sort each level's heights in descending order to allow easy access to the top two heights
        for depth in level_max_height:
            level_max_height[depth].sort(reverse=True)

        # Compute maximum height of the tree excluding each node's subtree
        for node_val in heights:
            depth = depths[node_val]
            max_heights = level_max_height[depth]

            # Determine the max height excluding the subtree at this node
            if len(max_heights) == 1:
                max_height_without_subtree[node_val] = depth - 1
            elif heights[node_val] == max_heights[0]:
                max_height_without_subtree[node_val] = depth + (max_heights[1] if len(max_heights) > 1 else 0)
            else:
                max_height_without_subtree[node_val] = depth + max_heights[0]

        # Step 3: Answer each query
        return [max_height_without_subtree[q] for q in queries]
