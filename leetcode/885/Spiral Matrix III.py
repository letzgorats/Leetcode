class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        # 우->하->좌->상
        spiral_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        current_direction = 0
        curr, curc = rStart, cStart
        answer = [[curr, curc]]
        steps = 1

        while len(answer) < rows * cols:

            for _ in range(2):
                for _ in range(steps):
                    curr += spiral_dir[current_direction][0]
                    curc += spiral_dir[current_direction][1]
                    if 0 <= curr < rows and 0 <= curc < cols:
                        answer.append([curr, curc])

                current_direction = (current_direction + 1) % 4

            steps += 1

        return answer