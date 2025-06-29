# solution 1 - (two pointers, sort) - (113ms) - (2025.06.29)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)

        # 미리 Pow(2,i) % MOD 계산
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        cnt = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                cnt += power[right - left]
                cnt %= MOD
                left += 1
            else:
                right -= 1

        return cnt