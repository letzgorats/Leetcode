# solution 1 - (math,greedy) - (59ms) - (2025.12.01)
from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        batteries.sort()
        total_energy = sum(batteries)

        i = len(batteries) - 1

        while i >= 0:
            if batteries[i] > total_energy // n:
                # 너무 큰 배터리는 평균 분배를 방해하므로
                # 그 배터리를 쓰는 컴퓨터는 "독립적으로" 계산하고
                total_energy -= batteries[i]
                # 나머지 컴퓨터(n-1)개에 대해 다시 평균을 구한다.
                n -= 1
            # 더 이상 큰 배터리가 평균(total_energy//n)보다 크지 않으면
            # 그 순간부터는 모든 배터리가 "평균 분배 가능"한 상태가 된다.
            else:
                break
            i -= 1

        # 모든 큰 배터리를 제거한 후 남은 total_energy를 남은 n개의 컴퓨터에
        # 나누면 그것이 최대 런타임이다.
        return total_energy // n

# solution 2 - (binary search) - (1553ms) - (2025.12.01)
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        batteries.sort()

        def is_valid(m):
            tmp = 0
            for b in batteries:
                tmp += min(b, m)

            if tmp >= m * n:
                return True
            return False

        left = min(batteries)
        right = sum(batteries) // n
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans