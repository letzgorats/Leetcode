# solution 1 - (dfs,bit manipulation,dfs,tree) - (2035ms) - (2025.07.24)
from collections import defaultdict
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)

        # 1. 트리 구성
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 2. 전처리 변수
        entry = [0] * n
        exits = [0] * n
        subtree_xor = [0] * n
        parent_of = [-1] * n
        time = 0

        # 3. DFS: entry/exit + subtree_xor + parent 기록
        def dfs(node, parent):
            nonlocal time
            parent_of[node] = parent
            entry[node] = time
            time += 1

            xor_val = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    xor_val ^= dfs(neighbor, node)

            subtree_xor[node] = xor_val
            exits[node] = time
            time += 1
            return xor_val

        dfs(0, -1)

        # 4. 포함관계 판별 함수
        def is_subtree(u, v):
            return entry[v] <= entry[u] <= exits[u] <= exits[v]

        total_xor = subtree_xor[0]
        res = float('inf')

        # 5. 간선 두 개 조합 탐색
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                u1, v1 = edges[i]
                u2, v2 = edges[j]

                # 항상 자식 노드를 서브트리 루트로 간주
                cut1 = u1 if parent_of[u1] == v1 else v1
                cut2 = u2 if parent_of[u2] == v2 else v2

                x = subtree_xor[cut1]
                y = subtree_xor[cut2]

                if is_subtree(cut1, cut2):
                    # cut1 ⊂ cut2
                    z = total_xor ^ y
                    y ^= x
                elif is_subtree(cut2, cut1):
                    # cut2 ⊂ cut1
                    z = total_xor ^ x
                    x ^= y
                else:
                    # 독립적인 두 서브트리
                    z = total_xor ^ x ^ y

                res = min(res, max(x, y, z) - min(x, y, z))

        return res


'''
간선 2개를 완전탐색으로 고르는 것 자체는 가능하다.
하지만, 그 이후에 xor을 새로 계산하는 방식때문에 시간초과가 난다.
(간선 2개 조합 + 매번 dfs -> O(n^2xn) = O(n^3) )

해결 방법
-> 1. 트리를 한 번의 dfs 로 전처리
    : 각 노드의 subtree_xor[node] 계산
    : entry/exit_time 을 이용해 누가 누구의 서브트리인지 빠르게 확인
-> 2. 그 뒤엔 각 조합마다
    : subtree_xor만 조합해서 계산
    : DFS 없이도 O(1) 에 xor 계산 가능
(간선 2개 조합 + 사전 전처리(subtree_xor) -> O(n^2) )

# node_a가 node_b의 서브트리 안에 있는지 판단
-> entry[b] <= entry[a] <= exits[a] <= exits[b]

# 해당 노드를 루트로 하는 서브트리의 xor 합
->  subtree_xor[node]  


# XOR 연산의 기본 성질 복습
| 성질          | 설명                   | 예시                     |
| ----------- | ----------------------| ----------------------- |
| `a ^ a = 0` | 같은 수 두 번 XOR하면 0   | `5 ^ 5 = 0`             |
| `a ^ 0 = a` | 0과 XOR하면 자기 자신     | `7 ^ 0 = 7`             |
| 교환/결합 법칙  | 순서 상관없이 묶어도 됨    | `a ^ b ^ c = c ^ a ^ b` |

# 어떤 부분 집합만 따로 빼고 싶을 때 어떻게 할까?
전체 XOR = a ^ b ^ c ^ d ^ e = T
특정 서브트리 i의 XOR = xi = b ^ c ^ d
이제 내가 구하고 싶은 건:
    -> val3 = 전체 xor 에서 xi 서브트리를 제외한 나머지 영역
    -> 그냥 T ^ xi 해주면 된다.

왜냐하면,

T = a ^ b ^ c ^ d ^ e
xi =      b ^ c ^ d

T ^ xi = (a ^ b ^ c ^ d ^ e) ^ (b ^ c ^ d)
       = a ^ e       ← b, c, d는 두 번 XOR되므로 사라짐!

즉,
| 계산                        | 의미                          |
| ------------------------- | --------------------------- |
| `total ^ xor[i]`          | 전체에서 i 서브트리 제거              |
| `xor[i] ^ xor[j]`         | i 내부에서 j 서브트리 제거 (j ⊂ i일 때) |
| `total ^ xor[i] ^ xor[j]` | 전체에서 i, j 모두 제거 (i ⊥ j)     |

| 상황                      | 계산식                              | 해석                    |
| ----------------------- | -------------------------------- | --------------------- |
| `j ⊂ i`                 | `val2 = xor[i] ^ xor[j]`         | i에서 j를 제거한 나머지        |
| `val3 = total ^ xor[i]` | 전체에서 i 서브트리 제거한 나머지              |                       |
| `i ⊂ j`                 | `val2 = xor[j] ^ xor[i]`         | j에서 i를 제거한 나머지        |
| `val3 = total ^ xor[j]` | 전체에서 j 서브트리 제거한 나머지              |                       |
| `i ⊥ j`                 | `val3 = total ^ xor[i] ^ xor[j]` | 전체에서 i, j 둘 다 제거한 나머지 |


'''

# another solution
import collections


class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # subtree_xor[i] = XOR sum of the subtree rooted at i
        # descendants[i] = set of all nodes in the subtree of i
        subtree_xor = [0] * n
        descendants = [set() for _ in range(n)]

        # Perform a post-order DFS from root 0 to populate our data structures
        def dfs(node, parent):
            # Initialize with the node's own value and self
            subtree_xor[node] = nums[node]
            descendants[node].add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    # After child returns, roll up its values
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    descendants[node].update(descendants[neighbor])

        # Start the traversal from node 0, with -1 as a placeholder parent
        dfs(0, -1)

        total_xor = subtree_xor[0]
        min_score = float('inf')

        # Iterate through all pairs of nodes (i, j) to represent the two cuts.
        # The cuts are the edges between i/j and their parents.
        # We start from 1 because node 0 is the root and has no parent edge to cut above it.
        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]

                # Case 1: j's subtree is inside i's subtree (nested cuts)
                if j in descendants[i]:
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i

                # Case 2: i's subtree is inside j's subtree (nested cuts)
                elif i in descendants[j]:
                    val1 = xor_i
                    val2 = xor_j ^ xor_i
                    val3 = total_xor ^ xor_j

                # Case 3: i and j are in independent branches
                else:
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j

                # Calculate score for this pair of cuts and update the minimum
                score = max(val1, val2, val3) - min(val1, val2, val3)
                min_score = min(min_score, score)

        return min_score