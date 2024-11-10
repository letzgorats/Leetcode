class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        if any(num > k for num in nums):
            return 1

        res = float("inf")
        bits = [0] * 32

        def bits_update(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res

        left = 0
        for right in range(len(nums)):
            bits_update(bits, nums[right], 1)

            cur_or = bits_to_int(bits)

            while left <= right and cur_or >= k:
                res = min(res, right - left + 1)
                bits_update(bits, nums[left], -1)
                cur_or = bits_to_int(bits)
                left += 1

        return -1 if res == float("inf") else res