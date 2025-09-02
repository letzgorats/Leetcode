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

# solution 1 - (math,coordinates) - (11ms) - (2025.09.02)
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: (x[0], -x[1]))
        ans = 0
        for i in range(0, len(points) - 1):
            (x1, y1) = points[i]
            lower = -1
            for j in range(i + 1, len(points)):
                (x2, y2) = points[j]
                if lower < y2 <= y1:  # y2 는 lower 보다는 "커야" 하고(중복 방지), y1 와는 작거나 같아도 된다.
                    ans += 1
                    lower = y2
                # if lower == y1: # lowe 가 y1 이면, 나머지는 볼 필요도 x
                #     break

        return ans