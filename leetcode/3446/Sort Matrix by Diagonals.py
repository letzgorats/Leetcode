# solution 1 - (heapq,matrix) - (54ms) - (2025.08.28)
import heapq
from typing import List
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)

        # middle diagonal~left bottom
        for i in range(n):
            q = []
            for j in range(i, n):
                heapq.heappush(q, -grid[j][j - i])
            # print(q)
            for j in range(i, n):
                grid[j][j - i] = -heapq.heappop(q)
            # print(grid)

        # middle diagonal~top right
        for i in range(1, n):
            q = []
            for j in range(n - i):
                heapq.heappush(q, grid[j][j + i])
            for j in range(n - i):
                grid[j][j + i] = heapq.heappop(q)
        # print(grid)
        return grid
# 0 1                 1 2
#   0 1
#   1 2

# 0                   2
#   0 2


# 0,1,2                 0,1,2
#         0 0
#         1 1
#         2 2
# 1,2                   0,1
#         1 0
#         2 1
# 2
#         2 0
'''
팁
1. 대각선만다 key 를 생각한다.
    - ↘: row - col
    - ↗: row + col
2. 시작점으로 생각한다.
    - 예) "왼쪽 열에서 시작해 ↘로 내려가자" -> (r,0), (r+1,1), (r+2,2),...
3. 직접 그려보기
    - 규칙이 보인다.

정리
    - ↘ : (i, j)에서 i-j는 항상 같음 → j = i - d
    - ↗ : (i, j)에서 i+j는 항상 같음 → j = c - i

'''

# solution 2 - (sort,matrix) - (11ms) - (2025.08.28)
import heapq
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)

        # 주대각선~왼아래(↙): 내림차순
        for i in range(n):
            q = []
            for j in range(i, n):
                q.append(grid[j][j - i])
            q.sort(reverse=True)
            t = 0
            for j in range(i, n):
                grid[j][j - i] = q[t]
                t += 1

        # 주대각선 위쪽(↗): 오름차순
        for i in range(1, n):
            q = []
            for j in range(n - i):
                q.append(grid[j][j + i])
            q.sort()
            t = 0
            for j in range(n - i):
                grid[j][j + i] = q[t]
                t += 1

        return grid
