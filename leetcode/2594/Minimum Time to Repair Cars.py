# solution 1 - binary search - (1031ms) - (2025.03.16)
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def is_valid(k):

            fixed = 0
            for r in ranks:
                # print("k=",k,"r=",r)
                # print(int(sqrt(k // r)))
                fixed += int(sqrt(k // r))
            if fixed >= cars:
                return True

            return False

        left, right = 1, min(ranks) * cars * cars

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):  # mid 로 수리가 가능하다면, 더 작은 시간안에도 수리가 가능한지 탐색
                right = mid - 1
            else:  # mid 로 수리하지 못한다면, 더 많은 시간으로 수리할 수 있는지 탐색
                left = mid + 1
        return left