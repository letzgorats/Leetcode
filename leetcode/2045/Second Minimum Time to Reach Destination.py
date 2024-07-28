from collections import defaultdict, deque


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # BFS 를 위한 큐 초기화 - 시작점 1번 노드
        q = deque([1])
        cur_time = 0  # 현재시간
        res = -1  # 첫 번째 도착 시간을 저장할 변수

        # 각 노드의 방문 시간을 저장할 딕셔너리
        visit_times = defaultdict(list)  # node -> [visit]

        while q:

            # 현재 레벨의 모든 노드를 처리
            for i in range(len(q)):
                node = q.popleft()

                # 목적지에 도달했을 때
                if node == n:
                    if res != -1:  # 이미 한 번 도착했다면, 이것이 두 번째 도착
                        return cur_time
                    res = cur_time  # 첫번째 도착시간을 저장

                # 인접한 노드들을 처리
                for nei in adj[node]:
                    nei_times = visit_times[nei]

                    # 아직 방문하지 않았거나, 한 번만 방문했고
                    # 현재 시간과 다른 경우에만 큐에 추가
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        nei_times.append(cur_time)

            # 신호등 처리 : 빨간불이면 다음 초록불까지 기다린다.
            if (cur_time // change) % 2 == 1:  # red light
                cur_time += change - (cur_time % change)

            # 다음 간선으로 이동
            cur_time += time

        return -1  # 두 번째 최단 경로를 찾지 못할 경우