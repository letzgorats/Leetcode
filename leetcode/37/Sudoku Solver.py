# solution 1 - (backtracking,brute force) - (2215ms) - (2025.08.31)
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 행, 열, 박스에 이미 들어간 숫자들을 기록
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        # 초기 상태 기록
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_id(r, c)].add(val)

        def backtrack(i=0):
            if i == len(empties):
                return True  # 다 채움

            r, c = empties[i]
            b = box_id(r, c)

            for num in map(str, range(1, 10)):  # '1' ~ '9'
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    # num을 넣어본다
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(i + 1):
                        return True

                    # 실패하면 되돌리기
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack()
