class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        # 1 -> once
        # 2 ~ n -> twice
        # 2 ~ n ->  distance = [j-i]

        answer = [0] * (2 * n - 1)
        visited = set()

        def backtracking(idx):

            if all(x != 0 for x in answer):  # 모든 숫자를 배치했다면(정답조건)
                return True

            if answer[idx] != 0:  # 이미 채워진 자리라면
                return backtracking(idx + 1)

            for num in range(n, 1, -1):  # 큰 숫자부터 배치

                if num in visited or num + idx >= len(answer) or answer[num + idx] != 0:  # 이미 num 이 사용되었거나, 공간이 부족하면 패스
                    continue

                # num 을 현재 위치에 배치(두번째 위치도 고려)
                answer[idx] = num
                answer[idx + num] = num
                visited.add(num)

                if backtracking(idx + 1):  # 재귀호출
                    return True  # 정답 찾음

                # 실패했다면, 되돌리기 백트래킹
                answer[idx] = 0
                answer[idx + num] = 0
                visited.remove(num)

            if 1 not in visited:
                answer[idx] = 1
                visited.add(1)

                if backtracking(idx + 1):  # 재귀 호출
                    return True

                # 실패하면 백트래킹
                answer[idx] = 0
                visited.remove(1)

            return False  # 어떤 숫자도 배치할 수 없으면 False

        backtracking(0)
        return answer