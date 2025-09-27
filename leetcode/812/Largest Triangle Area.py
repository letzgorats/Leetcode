# solution 1 - (math,bruteforce,combinations) - (77ms) - (2025.09.27)
from itertools import combinations
from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def shoelace_formula(x1, x2, x3, y1, y2, y3):
            return abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)) / 2

        three_points = list(combinations(points, 3))
        max_area = 0
        for lst in three_points:
            area = shoelace_formula(lst[0][0], lst[1][0], lst[2][0], lst[0][1], lst[1][1], lst[2][1])
            max_area = max(area, max_area)

        return max_area

'''
신발끈 공식
abs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)) / 2
'''