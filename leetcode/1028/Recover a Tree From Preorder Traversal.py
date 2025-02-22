# solution 1 - stack (20ms) - (2025.02.22)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        stack = []  # 깊이를 추적하는 스택
        i = 0  # 문자열 탐색을 위한 인덱스

        while i < len(traversal):
            # 1️⃣ 현재 노드의 깊이(level) 계산 ("-" 개수 세기)
            level = 0
            while i < len(traversal) and traversal[i] == "-":
                level += 1
                i += 1
            # print(i,level)
            # 2️⃣ 노드 값 가져오기 (여러 자리 숫자 처리)
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            node = TreeNode(value)  # 새로운 노드 생성

            # 3️⃣ 부모 노드 찾기 (스택을 이용해 level이 낮거나 같은 노드는 pop)
            while len(stack) > level:
                stack.pop()  # 현재 depth보다 높은 노드 제거

            # 4️⃣ 부모 노드와 연결
            # 스택(stack)에 저장된 노드는 실제 트리 노드 객체를 참조
            if stack:
                if not stack[-1].left:  # 왼쪽 자식이 없으면 왼쪽에 추가
                    # stack[-1].left = node 같은 할당을 하면 트리 내에서 해당 객체를 참조하는 모든 위치에서도 반영됨.
                    stack[-1].left = node
                else:  # 왼쪽 자식이 있으면 오른쪽에 추가
                    # stack[-1].right = node 같은 할당을 하면 트리 내에서 해당 객체를 참조하는 모든 위치에서도 반영됨.
                    stack[-1].right = node

            # 5️⃣ 스택에 현재 노드 추가 (깊이를 유지하면서 트리 구성)
            stack.append(node)
            # print("i=",i,"\n",stack)

        return stack[0]  # 루트 노드 반환

# solution 2 - dfs (20ms) - (2025.02.22)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        self.index = 0  # 현재 탐색중인 인덱스

        def dfs(level):

            if self.index >= len(traversal):
                return None

                # 현재 노드의 level 계산
            depth = 0
            while self.index < len(traversal) and traversal[self.index] == "-":
                depth += 1
                self.index += 1

            if depth != level:  # 현재 level 과 depth 가 다르면 부모 노드로 돌아가기
                self.index -= depth  # 인덱스를 롤백하여 부모 dfs 가 다시 해석하도록 함
                return None

            # 숫자 값 가져오기 (여러 자리 숫자 처리)
            value = 0
            while self.index < len(traversal) and traversal[self.index].isdigit():
                value = value * 10 + int(traversal[self.index])
                self.index += 1

            node = TreeNode(value)  # 새로운 노드 생성

            node.left = dfs(level + 1)
            node.right = dfs(level + 1)

            return node

        return dfs(0)


# solution 3 - dfs (27ms) - (2025.02.22)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        for i in range(100,0,-1):
            traversal = traversal.replace("-"*i,chr(i+65))

        # print(traversal)

        def function(result,depth):
            result = result.split(chr(depth+65))
            print(result)
            root = TreeNode(int(result[0]))
            root.left = function(result[1],depth+1) if len(result) > 1 else None
            root.right = function(result[2],depth+1) if len(result) > 2 else None
            return root

        return function(traversal,1)