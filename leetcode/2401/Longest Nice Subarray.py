# solution 1 - (bitwise, two pointers, sliding window) - (88ms) - (2025.03.18)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        l = 0
        or_sum = 0
        max_length = 1

        for r in range(len(nums)):

            while or_sum & nums[r]:  # 공통 비트가 있으면 윈도우 축소
                or_sum ^= nums[l]  # nums[l] 를 제거
                l += 1

            or_sum |= nums[r]  # nums[r] 추가
            max_length = max(max_length, r - l + 1)

        return max_length

    '''
    or_sum 의 역할

    현재 윈도우 내 모든 숫자의 OR 값을 유지해서,
    새로운 숫자(nums[r])를 추가할 때 겹치는 비트가 있는지 즉시 확인할 수 있음.
    비트가 겹치는지 확인하는 빠른 방법

    or_sum & nums[r] == 0이면 OK → 추가 가능
    or_sum & nums[r] != 0이면 NO → l을 이동하여 축소

    슬라이딩 윈도우의 최적화된 상태 유지

    or_sum |= nums[r] (새로운 숫자 추가)
    or_sum ^= nums[l] (비트가 겹치면 윈도우에서 숫자 제거)
    '''

