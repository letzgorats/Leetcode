# solution 1 - 3132 ms
from collections import deque
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        def rotate_90(matrix):
            n = len(matrix)
            m = len(matrix[0])
            new = [['.'] * n for _ in range(m)]

            for i in range(n):
                for j in range(m):
                    new[j][n - 1 - i] = matrix[i][j]
            return new

        rotated_matrix = rotate_90(box)

        n = len(rotated_matrix)
        m = len(rotated_matrix[0])

        q = deque([])
        # 밑에서부터 돌이 있는 위치 저장
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if rotated_matrix[i][j] == '#':
                    q.append((i, j))

        # 중력 작용
        while q:
            r, c = q.popleft()
            nr, nc = r + 1, c
            while 0 <= nr < n:
                if 0 <= nr < n:
                    if rotated_matrix[nr][nc] == '.':  # 빈칸이면 그대로 중력작용
                        rotated_matrix[nr][nc] = rotated_matrix[nr - 1][c]
                        rotated_matrix[nr - 1][c] = '.'
                    else:
                        break
                else:
                    break
                nr += 1

        return rotated_matrix

# solution 2 - col two pointers 1920ms
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        n, m = len(box), len(box[0])
        for r in range(n):
            i = m - 1  # start : last position, i -> next empty spot
            for c in reversed(range(m)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c - 1

        res = []

        for c in range(m):
            col = []
            for r in reversed(range(n)):
                col.append(box[r][c])
            res.append(col)

        return res

# solution 3 - 1877ms
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        n, m = len(box), len(box[0])

        res = [["."] * n for _ in range(m)]

        for r in range(n):
            i = m - 1  # start : last position, i -> next empty spot
            for c in reversed(range(m)):
                if box[r][c] == "#":
                    res[i][n - r - 1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    res[c][n - r - 1] = "*"
                    i = c - 1

        return res

