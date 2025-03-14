# solution 1 - binary search - (561ms) - (2025.03.14)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if k > sum(candies):
            return 0

        def is_valid(m):

            threshold = 0
            for candy in candies:
                if candy == m:
                    threshold += 1
                elif candy > m and m != 0:
                    threshold += candy // m
            # print(threshold)
            if k <= threshold:
                return True
            return False


        left, right = 0, max(candies)
        answer = 1
        while left <= right:
            mid = (left+right) // 2

            if is_valid(mid):   # mid 로 분배 가능하면 더 큰 mid 탐색
                answer = max(answer,mid)
                left = mid + 1
            else:   # mid 로 분배 불가능하면 더 작은 mid 탐색
                right = mid - 1
            # print(answer)
        return answer

# solution 2 - binary search - (229ms) - (2025.03.14)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if k > sum(candies):
            return 0

        def is_valid(m):

            threshold = 0
            for candy in candies:
                if candy == m:
                    threshold += 1
                elif candy > m and m != 0:
                    threshold += candy // m
            # print(threshold)
            if k <= threshold:
                return True
            return False


        left, right = 1, sum(candies) // k
        answer = 1
        while left <= right:
            mid = (left+right) // 2

            if is_valid(mid):   # mid 로 분배 가능하면 더 큰 mid 탐색
                answer = mid    # answer 에 바로 답을 할당하기 - 어차피 binary search 는 최적해 보장
                left = mid + 1
            else:   # mid 로 분배 불가능하면 더 작은 mid 탐색
                right = mid - 1
            # print(answer)
        return answer

