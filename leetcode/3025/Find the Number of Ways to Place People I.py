# Wrong answer - () - () - (2025.09.02)
import heapq
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: (x[0], -x[1]))
        # print(points)

        ans = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            if x1 <= x2 and y1 >= y2:
                ans += 1

        return ans

# solution 1 - () - () - (2025.09.02)
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: (x[0], -x[1]))

        floor = float('inf')
        ans = 0
        for i in range(0, len(points)):
            (x1, y1) = points[i]
            floor = min(y1, floor)  # 지금까지 만난 가장 낮은 y

            # 3. j를 오른쪽 아래 후보로 훑음
            for j in range(i + 1, len(points)):
                (x2, y2) = points[j]

                # 위치 조건: 오른쪽에 있어야 하고 더 아래에 있어야 함
                if x2 > x1 and y2 <= y1:

                    # 새로운 "더 낮은 y"가 나오면 유효한 쌍
                    if y2 < floor:
                        ans += 1
                        floor = y2

                    # y2 == floor 이면 이미 같은 y의 점이 있어서 경계에 걸리므로 skip
                    # y2 > floor 인 경우는 사각형 안에 들어와 버림 → skip

        return ans