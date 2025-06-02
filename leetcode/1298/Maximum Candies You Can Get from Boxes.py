# solution 1 - (bfs,simultaion) - (23ms) - (2025.06.03)
from collections import deque
import heapq
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        have_keys = set()
        for idx, s in enumerate(status):
            if s == 1:  # openable box
                have_keys.add(idx)

        boxes = deque(initialBoxes)

        tmp = 0
        visited = set()
        left = set()

        while True:

            changed = False
            new_boxes = deque()

            while boxes:
                box = boxes.popleft()
                if box in visited:
                    continue

                if (status[box] == 1) or (box in have_keys):  # openable
                    visited.add(box)
                    tmp += candies[box]
                    changed = True

                    # 열쇠 얻기
                    for k in keys[box]:
                        have_keys.add(k)

                    # 새로운 상자 얻기
                    for b in containedBoxes[box]:
                        new_boxes.append(b)
                else:
                    left.add(box)

            # previously skipped boxes 중에서 열 수 있게 된 애들 다시 넣기
            reopened = list(left & have_keys)
            for b in reopened:
                new_boxes.append(b)
                left.remove(b)
                changed = True

            if not changed:
                break  # 더 이상 새로 열린 상자 없음

            boxes = new_boxes  # 다음 턴에 다시 처리할 상자들

        return tmp


# Wrong answer
from collections import deque
import heapq


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        # q = [] # openable box(keys)
        have_keys = set()
        for idx, s in enumerate(status):
            if s == 1:  # openable box
                have_keys.add(idx)

        boxes = deque(initialBoxes)

        tmp = 0
        # visited = set()
        left = set()
        while boxes:

            box = boxes.popleft()
            if (status[box] == 1) or (box in have_keys):  # openable
                # visited.add(box)
                tmp += candies[box]
            else:
                left.add(box)

            for k in keys[box]:
                have_keys.add(k)

            for b in containedBoxes[box]:
                boxes.append(b)

        # print(have_keys)
        # print(left)
        s = list(left & have_keys)
        for i in s:  # openable
            tmp += candies[i]

        return tmp


'''
Wrong answer 코드에서의 실수

1. left & have_keys 의 교집합은 단 1회만 처리
열 수 있는 박스를 다시 큐에 넣지 않고 단순히 tmp += candies[i] 로 끝냄
-> 하지만 그 상자 안에 또 다른 열쇠나 상자가 있을 수도 있음 → 무시됨

2. 재귀적인 상태 변화가 없음
시뮬레이션 문제의 핵심인 "열쇠를 얻으면 새로운 길이 열린다" 를 1회만 처리하고 끝냄
-> while 루프를 통해 상태 변화가 없을 때까지 반복했어야 함

3. 🔒 visited 처리가 없어서 같은 상자 중복 처리 가능성 존재 (예: 무한 루프 위험성)
-> 썼다가 필요없는 것 같아서 지웠는데, 단순 BFS가 아니라 상태변화가 생기는 시뮬레이션 유형이므로 필요함.
-> 따라서, "더 이상 열 수 있는 상자가 없을 때까지 상태 변화 시뮬레이션"이 필요하다.
'''