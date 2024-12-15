import heapq
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
