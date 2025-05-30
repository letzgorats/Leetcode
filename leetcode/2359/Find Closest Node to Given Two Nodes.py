# TLE - (tree,bfs) - (TLE) - (2025.05.30)
from collections import defaultdict, deque
from typing import List
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        graph = defaultdict(list)

        for idx, node in enumerate(edges):
            if node != -1:
                graph[idx].append(node)

        # print(graph)

        n = len(edges)
        distance_from_node1 = [[False, 0] for _ in range(n)]
        distance_from_node2 = [[False, 0] for _ in range(n)]

        def bfs(source, distance):

            q = deque([(source, 0)])  # start_node, dist
            visited = set()
            visited.add(source)
            while q:

                curr, dist = q.popleft()
                distance[curr] = [True, max(distance[curr][1], dist)]
                for nxt in graph[curr]:
                    if nxt not in visited:
                        q.append((nxt, dist + 1))

            return distance

        distance_from_node1 = bfs(node1, distance_from_node1)
        distance_from_node2 = bfs(node2, distance_from_node2)

        # print(distance_from_node1)
        # print(distance_from_node2)

        answer = -1
        tmp = 10 ** 5
        for idx in range(n):

            if distance_from_node1[idx][0] and distance_from_node2[idx][0]:
                dist = max(distance_from_node1[idx][1], distance_from_node2[idx][1])
                if tmp > dist:
                    tmp = dist
                    answer = idx
                    # break

        return answer

# solution 1 - (tree,bfs) - (95ms) - (2025.05.30)
from collections import defaultdict, deque


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def get_distance(source):

            distance = [-1] * len(edges)
            curr = source
            dist = 0
            while curr != -1 and distance[curr] == -1:
                distance[curr] = dist
                dist += 1
                curr = edges[curr]

            return distance

        n = len(edges)
        distance_from_node1 = get_distance(node1)
        distance_from_node2 = get_distance(node2)

        # print(distance_from_node1)
        # print(distance_from_node2)

        answer = -1
        tmp = 10 ** 5
        for idx in range(n):

            if distance_from_node1[idx] != -1 and distance_from_node2[idx] != -1:
                dist = max(distance_from_node1[idx], distance_from_node2[idx])
                if tmp > dist:
                    tmp = dist
                    answer = idx

        return answer

'''
| 항목                | 기존 풀이                                                | 최적 풀이                                  |
| ----------------- | ---------------------------------------------------- | -------------------------------------- |
| 그래프 표현        | `defaultdict(list)`로 인접 리스트 생성                       | `edges[i]` 배열 자체를 그대로 활용 (불필요한 리스트 제거) |
| 탐색 방식         | `deque`를 이용한 BFS 탐색                                  | 단순 while-loop로 경로를 따라 이동               |
| 거리 기록 방식      | `[visited, distance]` 형태의 배열로 관리                     | `-1`로 초기화된 거리 배열 하나로 미방문 여부 및 거리 모두 표현 |
| 시간 복잡도        | O(n) 같지만 실제 구현에서 큐와 리스트 사용으로 오버헤드 발생 → TLE 발생 가능 | O(n), 각 노드를 **딱 한 번**만 방문하며 매우 효율적     |
| 정답 선택 로직      | `break` 사용으로 더 나은 후보를 무시하는 경우 발생 가능(이건 break 없애줌) | 모든 노드 탐색하며 최적의 조건 만족하는 노드 선택 (안정적)     |
| 코드 가독성 및 유지보수 | 구조가 복잡하고 변수 많음                                       | 매우 간결하고 구조적으로 명확함                      |
'''

'''
- 이 문제는 그래프가 최대 한 방향으로만 이어지므로, 일반적인 그래프 탐색 로직(BFS/DFS)가 필요 없다.
- edges[i] 가 곧 다음 노드를 의미하므로, 그냥 while 문으로 따라가며 거리만 기록하면 됐다. (그래프를 따로 만들 필요없이 바로 거리 추적 가능)
- 방문 여부 -1 거리 여부로 충분히 판별 가능하므로, visited 같은 별도 구조도 불필요했다.
'''