class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        max_val = (1 << maximumBit) - 1

        cal_xor = 0
        for num in nums:
            cal_xor ^= num

        res = []
        for num in reversed(nums):
            res.append(cal_xor ^ max_val)

            cal_xor ^= num

        return res