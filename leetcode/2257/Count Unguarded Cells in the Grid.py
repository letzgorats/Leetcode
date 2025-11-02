# solution 4 - (simulation,bfs) - (608ms) - (2025.11.02)
from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        board = [[0 for _ in range(n)] for _ in range(m)]
        # print(board)
        total = n * m
        for r, c in walls:
            board[r][c] = 1

        def bfs(r, c):

            q = deque([(r, c)])
            while q:

                r, c = q.popleft()
                for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr = r + d[0]
                    nc = c + d[1]
                    while 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 0:
                        surveillance.add((nr, nc))
                        nr += d[0]
                        nc += d[1]

        surveillance = set()
        for r, c in guards:
            board[r][c] = 1

        for r, c in guards:
            bfs(r, c)

        # print(surveillance)
        return total - len(surveillance) - len(guards) - len(walls)


# solution 1 - (greedy,simulation) - (329ms) - (2024.11.21)
from collections import deque
from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        board = [[0] * n for _ in range(m)]

        for r, c in walls:
            board[r][c] = 1
        for r, c in guards:
            board[r][c] = 1

        q = deque(guards)
        while q:

            r, c = q.popleft()
            for j in range(r - 1, -1, -1):
                if board[j][c] == 1:
                    break
                elif board[j][c] != 1:
                    board[j][c] = 2

            for j in range(r + 1, m):
                if board[j][c] == 1:
                    break
                elif board[j][c] != 1:
                    board[j][c] = 2

            for j in range(c - 1, -1, -1):
                if board[r][j] == 1:
                    break
                elif board[r][j] != 1:
                    board[r][j] = 2

            for j in range(c + 1, n):
                if board[r][j] == 1:
                    break
                elif board[r][j] != 1:
                    board[r][j] = 2

        answer = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    answer += 1

        return answer


# solution 2 - (greedy,simulation) - (315ms) - (2024.11.21)
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        board = [[0] * n for _ in range(m)]

        # 0 = free, 1 = guard, 2 = wall, 3 = guardable

        for r, c in guards:
            board[r][c] = 1
        for r, c in walls:
            board[r][c] = 2

        def mark_guarded(r, c):

            for row in range(r + 1, m):
                if board[row][c] in [1, 2]:
                    break
                board[row][c] = 3

            for row in reversed(range(0, r)):
                if board[row][c] in [1, 2]:
                    break
                board[row][c] = 3

            for col in range(c + 1, n):
                if board[r][col] in [1, 2]:
                    break
                board[r][col] = 3

            for row in reversed(range(0, c)):
                if board[r][col] in [1, 2]:
                    break
                board[r][col] = 3

        for r, c in guards:
            mark_guarded(r, c)

        res = 0
        for row in board:
            for n in row:
                if n == 0:
                    res += 1
        return res

# solution 3 - (bfs) - (241ms) - (2024.11.21)
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        board = [[0] * n for _ in range(m)]

        # mark guards and walls as 2

        for r, c in guards:
            board[r][c] = 2
        for r, c in walls:
            board[r][c] = 2

        # directions : up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r, c
                while True:
                    nr += dr
                    nc += dc
                    # check cells in current direction until hitting boundary or obstacle
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or board[nr][nc] == 2:
                        break
                    board[nr][nc] = 1  # guardable

        # count unguarded cells
        return sum(row.count(0) for row in board)