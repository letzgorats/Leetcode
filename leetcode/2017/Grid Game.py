class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])

        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]

        for i in range(1,n):
            top_prefix[i] = top_prefix[i-1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i-1] + grid[1][i]

        answer = float('inf')

        for j in range(n):

            # j 번째 열에서 첫 번째 로봇이 아래로 내려간다고 가정

            # 나머진 0으로 바뀌니까 첫 번째 행에서
            # 두번째 로봇이 얻을 수 있는 남은 점수
            top_remaining = top_prefix[n-1] - top_prefix[j]

            # 내려와서 나머진 0으로 바뀌니까 두 번째 행에서
            # 두번째 로봇이 얻을 수 있는 남은 점수
            bottom_remaining = bottom_prefix[j-1] if j > 0 else 0

            # 두 값중에 큰 값 비교
            second_robot_score = max(top_remaining,bottom_remaining)

            # 가능한 second_robot_score 값들 중 최솟값을 선택해야 한다.
            # 첫번째 로봇의 임무가 두번째 로봇의 점수를 최소화하는 것이기 때문이다.
            answer = min(answer,second_robot_score)

        return answer