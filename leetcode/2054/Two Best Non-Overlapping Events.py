import heapq
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        n = len(events)  # 작업의 총 개수

        # event를 시작시간에 따라 정렬 - 순차적으로 작업을 순회하기 위함
        events = sorted(events, key=lambda x: x[0])

        q = []
        current_max = 0  # 현재까지 종료된 이벤트 중 최대 가치
        max_value = 0  # 두 이벤트를 선택한 최대 가치

        for s, e, v in events:

            # 현재 event의 시작 시간 이전에 끝나는 작업들을 heap에서 제거
            while q and q[0][0] < s:
                _, value = heapq.heappop(q)
                # 현재 event시작 시간 이전에 끝나는 event들 중 최대 수익
                current_max = max(current_max, value)

            # 첫 번째 evnet의 최대 가치와 현재 event의 가치를 합산
            max_value = max(max_value, current_max + v)

            # 현재 event를 힙에 추가 (종료 시간, 가치)
            heapq.heappush(q, (e, v))

        return max_value