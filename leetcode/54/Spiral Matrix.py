# my solution

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        answer = []

        n = len(matrix)
        m = len(matrix[0])

        curr, curc = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        answer.append(matrix[curr][curc])
        cur_dir = 0
        visit = set()
        visit.add((0, 0))

        for _ in range(n * m - 1):

            nr = curr + direction[cur_dir][0]
            nc = curc + direction[cur_dir][1]
            if nr < 0 or nr >= n or nc < 0 or nc >= m or (nr, nc) in visit:
                cur_dir = (cur_dir + 1) % 4
                nr = curr + direction[cur_dir][0]
                nc = curc + direction[cur_dir][1]

            curr, curc = nr, nc
            visit.add((curr, curc))
            answer.append(matrix[curr][curc])

        return answer


# different solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        answer = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # move right
            for i in range(left, right + 1):
                answer.append(matrix[top][i])
            top += 1

            # move down
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # move left
                for i in range(right, left - 1, -1):
                    answer.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # move up
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1

        return answer