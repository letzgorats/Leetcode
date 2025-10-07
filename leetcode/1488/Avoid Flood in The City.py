# solution 1 - (hepaq,deque,priority queue) - (237ms) - (2025.10.07)
from collections import defaultdict, deque
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        lakes = defaultdict(deque)
        # 0일 때 어떤 호수를 말릴지 결정할 때, 단순히 현재 찬 호수 중 아무거나 고르면 안되고,
        # 미래에 다시 비가 올 호수를 우선적으로 말려야 한다.

        # 1. 각 호수에 대해 비가 오는 날들의 인덱스 목록을 미리 만들고(미래 정보 준비)
        # 2. 어떤 호수 x에 비가 오면, 그 호수에 다음에 비가 오는 날(next_idx)를 찾아
        #    min heap에 (next_idx,x) 로 넣으면 된다.
        # 3. 0(말릴 수 있는 날)이 오면, heap에서 가장 시급한(가장 빨리 다시 비가 오는)호수를
        #    꺼내 그 호수를 말린다.

        for i in range(len(rains)):
            if rains[i] != 0:
                lakes[rains[i]].append(i)

        ans = [-1] * len(rains)
        full = set()  # 현재 물이 찬 호수들
        q = []  # (다음에 비오는 인덱스, lake)

        for i, x in enumerate(rains):

            if x > 0:
                # 오늘 x호수에 비가 옴
                if x in full:
                    return []  # 홍수->[]
                full.add(x)
                ans[i] = -1
                # 이번 i를 소비했으니 pop
                lakes[x].popleft()
                # 다음에 또 비가 오는 날이 있다면, 그 데드라인을 heap 에 넣어야 한다.
                if lakes[x]:
                    next_idx = lakes[x][0]
                    heapq.heappush(q, (next_idx, x))

            else:
                # 건조하는 날
                if q:
                    # 가장 빨리 비가 올 호수부터 말린다.
                    _, lake = heapq.heappop(q)
                    full.remove(lake)
                    ans[i] = lake
                else:
                    # 아무거나 말려도 된다.
                    ans[i] = 1

        return ans