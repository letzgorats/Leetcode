
# solution1 - dp
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if sqrt(n) == int(sqrt(n)):
            return 1

        dp = [i for i in range(n+1)]

        
        for i in range(1,n+1):
            j = 1
            while j ** 2 <= i: 
                dp[i] = min(dp[i],dp[i-j**2]+1)
                j += 1
        # print(dp)
        return dp[n]


# solution2 - BFS

from collections import deque
class Solution(object):
    def numSquares(self, n):

        # 가능한 모든 완전 제곱수를 미리 계산
        squares = [i**2 for i in range(1,int(sqrt(n))+1)]

        queue = deque([(n,0)])
        visited = {n}

        while queue:

            remainder, steps = queue.popleft()
            # 가능한 모든 완전 제곱수에 대해
            for square in squares:
                next_remainder = remainder - square
                # 정확히 0에 도달하면, 현재 단계 수를 반환
                if next_reaminder == 0:
                    return steps + 1
                # 아직 방문하지 않은 숫자만 큐에 추가
                elif next_remainder > 0 and next_remainder not in visited:
                    visited.add(next_remainder)
                    queue.append((next_remainder,steps+1))
                # next_remainder가 0보다 작으면 더 이상 탐색하지 않음
                elif next_remainder < 0:
                    break
        return 0  # 이론상 여기에 도달할 수 없음, 모든 숫자는 완전 제곱수의 합으로 표현 가능
        
