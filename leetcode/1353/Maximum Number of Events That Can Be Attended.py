# solution 1 - (priority queue,heapq,greedy,monotonic stack) - (147ms) - (2025.07.07)
import heapq
from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort()
        q = []
        i = 0
        day = 1
        res = 0
        n = len(events)

        # 최대 day는 가장 늦게 끝나는 날까지만 돌면 된다.
        max_day = max(e for _, e in events)

        while day <= max_day:
            # 그 날 시작하는 이벤트들을 힙에 추가
            while i < n and events[i][0] == day:
                heapq.heappush(q, events[i][1])  # 종료일만 힙에 넣음
                i += 1
            # print(q)
            # 이미 지난 이벤트 제거
            while q and q[0] < day:
                heapq.heappop(q)

            # 오늘 하나 참석 가능하면 참석
            if q:
                heapq.heappop(q)
                res += 1    # 하루에 한개만 참여
            # print(res)

            day += 1

        return res