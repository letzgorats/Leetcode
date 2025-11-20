# MLE, TLE - (sort,set) - (TLE) - (2025.11.20)
from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        numbers = set()

        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
        # print(intervals)

        for a, b in intervals:

            if len(numbers & set([i for i in range(a, b + 1)])) == 0:
                numbers.add(b)
                numbers.add(b - 1)
            elif len(numbers & set([i for i in range(a, b + 1)])) == 1:
                numbers.add(b)

        # print(numbers)

        return len(numbers)


'''
| 코드         | 점검 범위                            | 시간 복잡도                                   |
| ---------- | -------------------------------- | ---------------------------------------- |
| 통과 코드  | numbers 내부의 실제 선택된 점들만 검사        | O(N) 수준                                  |
| TLE 코드 | interval 전체 길이(a~b)를 매번 set으로 만듦 | O(N × interval_length) → 최악 10⁵ × 10⁵ 불가 |

'''

# solution 1 - (sort,set) - (266ms) - (2025.11.20)
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        numbers = set()
        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))

        for start, end in intervals:
            count = 0
            for x in numbers:
                if start <= x <= end:
                    count += 1

            if count == 0:
                numbers.add(end - 1)
                numbers.add(end)
            if count == 1:
                numbers.add(end)

        return len(numbers)
