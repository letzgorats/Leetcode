# solution 1 - set 1000 if visited, and new_count(28ms)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        answer = 0

        # Step 1: 행 기준 처리
        for i in range(n):
            row_sum = sum(grid[i])
            if row_sum >= 2:  # 행에서 연결된 서버가 2개 이상인 경우
                answer += row_sum
                for j in range(m):
                    if grid[i][j] == 1:  # 서버를 1000으로 변경
                        grid[i][j] = 1000

        # Step 2: 열 기준 처리
        for j in range(m):
            col_sum = 0
            count_new = 0  # 새롭게 발견된 서버 수

            for i in range(n):
                if grid[i][j] == 1000:  # 이미 행에서 처리된 서버
                    col_sum += 1000
                elif grid[i][j] == 1:  # 새롭게 발견된 서버
                    col_sum += 1
                    count_new += 1

            if col_sum >= 2000:  # 행에서 처리된 서버와 연결된 경우
                answer += count_new  # 새롭게 발견된 서버만 더하기

            # 새로운 서버와 이미 처리된 서버를 합산
            elif count_new + col_sum // 1000 >= 2:
                answer += count_new

        return answer

# solution 2 - simplication(20ms)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        answer = 0

        # Step 1: 행 기준 처리
        for i in range(n):
            row_sum = sum(grid[i])
            if row_sum >= 2:  # 행에서 연결된 서버가 2개 이상인 경우
                answer += row_sum
                for j in range(m):
                    if grid[i][j] == 1:  # 서버를 1000으로 변경
                        grid[i][j] = 1000

        # Step 2: 열 기준 처리
        for j in range(m):
            col_sum = 0
            for i in range(n):
                col_sum += grid[i][j]

            # 행에서 발견됐던 서버수 + 새롭게 발견된 서버수 >= 2
            if col_sum // 1000 + col_sum % 1000 >= 2:
                answer += col_sum % 1000  # 새롭게 발견된 서버수만 더해준다.

        return answer

# solution 3 - public solution
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        answer = 0

        row_count = [0] * n
        col_count = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # print(row_count)
        # print(col_count)
        answer = 0
        for i in range(n):
            for j in range(m):
                # 각 서버에 대해, 그 서버가 속한 행과 열에 2개 이상의 서버가 있으면
                # 그 서버는 연결된 서버로 취급한다.
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    # 행 또는 열에 연결된 서버는 한 번만 카운트, 중복 계산 방지
                    answer += 1

        return answer