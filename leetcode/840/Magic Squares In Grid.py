class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0

        def isMagic(r, c):

            once = [False] * 10
            rowSum = [0, 0, 0]
            colSum = [0, 0, 0]

            for a in range(r - 1, r + 2):
                for b in range(c - 1, c + 2):
                    tmp = grid[a][b]
                    if tmp < 1 or tmp > 9: return False
                    rowSum[a - r + 1] += tmp
                    colSum[b - c + 1] += tmp
                    if once[tmp]:
                        return False
                    once[tmp] = True

            for b in once[1:]:
                if not b: return False

            for sums in rowSum:
                if sums != 15: return False
            for sums in colSum:
                if sums != 15: return False

            return grid[r - 1][c - 1] + grid[r + 1][c + 1] == 10 and grid[r + 1][c - 1] + grid[r - 1][c + 1] == 10

        # 3x3 Magic square has 5 in the middle.
        # Use this fact to save computational time.
        answer = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if isMagic(i, j):
                    answer += 1

        return answer


