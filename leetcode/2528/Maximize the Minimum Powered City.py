# solution 1 - (prefix sum,difference array,binary search) - (1022ms) - (2025.11.07)
from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        n = len(stations)
        cnt = [0] * (n + 1)  # 차분배열

        for i in range(n):
            left = max(0, i - r)  # 이 발전소가 전력을 주기 시작하는 도시의 인덱스
            right = min(n, i + r + 1)  # 여기서 끝 다음 인덱스(차분배열 이용하려고)
            cnt[left] += stations[i]  # 더해주고
            cnt[right] -= stations[i]  # 빼주고

        print(cnt)

        # 모든 도시의 전력을 최소 val 이상으로 만들 수 있는가?
        def is_valid(val):
            diff = cnt[:]
            total = 0
            remaining = k

            for i in range(n):
                total += diff[i]  # 지금 도시 i의 전력 = 이전까지의 누적 + diff[i]
                if total < val:  # 부족하면
                    add = val - total
                    if remaining < add:
                        return False
                    remaining -= add
                    # 발전소 add개 를 어디에 지을까?
                    end = min(n, i + 2 * r + 1) # [(i+r)-r ~ (i+r)+r)]
                    diff[end] -= add
                    total += add
            return True

        lo, hi = min(stations), sum(stations) + k
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_valid(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res