# solution 1 - (heapq) - (1309ms) - (2024.12.15)
import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        q = []
        for a, b in classes:
            current_ratio = a / b
            increment = (a + 1) / (b + 1) - current_ratio
            # 증가율을 음수로 저장
            heapq.heappush(q, (-increment, a, b))

        while extraStudents > 0:
            _, a, b = heapq.heappop(q)
            a += 1
            b += 1
            new_increment = (a + 1) / (b + 1) - (a / b)
            heapq.heappush(q, (-new_increment, a, b))
            extraStudents -= 1

        answer = 0
        while q:
            _, a, b = heapq.heappop(q)
            answer += a / b

        return answer / len(classes)


# solution 2 - (heapq) - (1258ms) - (2025.09.01)
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        """
        # extraStudents를 각 그룹에 투입했을 때, 비율이 가장 높아지는 그룹을 선택
        # -> 증가율이 높아지는 순으로 힙큐에 저장
        # 초기 설정
        """

        q = []  # max heap
        for p, t in classes:
            current_ratio = p / t
            increment = (p + 1) / (t + 1) - current_ratio
            heapq.heappush(q, (-increment, p, t))

        # print(q)

        while extraStudents:
            _, p, t = heapq.heappop(q)
            # assign student
            p += 1
            t += 1
            # 새로운 증가율
            new_inc = (p + 1) / (t + 1) - p / t
            heapq.heappush(q, (-new_inc, p, t))
            extraStudents -= 1

        # print(q)

        ans = 0.0
        while q:
            ratio, p, t = heapq.heappop(q)
            ans += (p / t)

        return ans / len(classes)

