import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        left = 1
        right = max(quantities)

        def canDistribute(stores):

            total_stores_needed = 0
            for q in quantities:
                total_stores_needed += math.ceil(q / stores)
                if total_stores_needed > n:  # 상점 n 초과시
                    return False

            return total_stores_needed <= n

        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left