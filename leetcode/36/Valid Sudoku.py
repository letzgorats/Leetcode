# solution 1 - (matrix,grid,row,col) - (7ms) - (2025.08.30)
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_3x3():

            count = set()
            for i in range(3):
                for j in range(3):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(3, 6):
                for j in range(3):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False
            count = set()
            for i in range(6, 9):
                for j in range(3):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(3):
                for j in range(3, 6):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(3, 6):
                for j in range(3, 6):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(6, 9):
                for j in range(3, 6):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(3):
                for j in range(6, 9):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(3, 6):
                for j in range(6, 9):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            count = set()
            for i in range(6, 9):
                for j in range(6, 9):
                    if board[i][j] != ".":
                        if board[i][j] not in count:
                            count.add(board[i][j])
                        else:
                            return False

            return True

        def is_valid(r, c):

            count = [0] * 10
            # check row
            for i in range(9):
                if board[i][c] != ".":
                    count[int(board[i][c])] += 1
                    if count[int(board[i][c])] > 1:
                        return False

            count = [0] * 10
            # check col
            for j in range(9):
                if board[r][j] != ".":
                    count[int(board[r][j])] += 1
                    if count[int(board[r][j])] > 1:
                        return False
            return True

        if check_3x3():

            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        if not is_valid(i, j):
                            return False

            return True

        else:
            return False

# solution 2 - (matrix,grid,row,col) - (0ms) - (2025.08.30)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        # box_id = (r//3)*3 + (c//3)
        boxes = [set() for _ in range(9)]
        '''
        0 1 2
        3 4 5
        6 7 8
        '''

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                b = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        return True


'''
b = (r//3) * 3 + (c//3) 로 3x3 박스 인덱스(0~8)계산
set 3종(행/열/박스) 만 유지 -> 중복 나오면 즉시 False
각 칸을 한번만 방문 -> 깔끔하고 빠름.
'''