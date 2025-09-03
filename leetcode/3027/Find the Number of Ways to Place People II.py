# solution 1 - (math,sorting) - (1456ms) - (2025.09.03)
from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[0], -x[1]))
        ans = 0
        for i in range(0, len(points) - 1):
            (x1, y1) = points[i]
            lower = float('-inf')
            for j in range(i + 1, len(points)):
                (x2, y2) = points[j]
                if lower < y2 <= y1:  #
                    ans += 1
                    lower = y2
                # if lower == y1: # lowe 가 y1 이면, 나머지는 볼 필요도 x
                #     break

        return ans