# solution 1 - helpㅎ(valid) function

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def canAchievePenalty(penalty):

            operations = 0
            for balls in nums:

                if balls > penalty:
                    operations += (balls - 1) // penalty

            return operations <= maxOperations

        left = 1
        right = max(nums)

        while left < right:

            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid
            else:
                left = mid + 1

        return left

# solution 2 - one line
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            # 탐색하려는 최소 가방 사이즈
            mid = (left + right) // 2
            # 가방사이즈를 다 나누어 보아서, 필요한 연산 수를 체크
            if sum((num - 1) // mid for num in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid

        return left