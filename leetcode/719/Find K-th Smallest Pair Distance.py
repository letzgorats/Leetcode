class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]

        while low <= high:

            mid = (low + high) // 2
            cnt = 0

            left = 0
            for right in range(n):

                # 거리가 mid 보다 큰 경우 left 를 이동
                while nums[right] - nums[left] > mid:
                    left += 1
                cnt += right - left

            # k 보다 적으면 더 큰 범위에서 탐색
            if cnt < k:
                low = mid + 1
            # k 보다 크거나 같으면, 더 작은 범위에서 탐색
            else:
                high = mid - 1

        return low


