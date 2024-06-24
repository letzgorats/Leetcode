class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flip = [0] * n

        current_flips = 0
        result = 0

        for i in range(n):

            if i >= k:
                current_flips -= flip[i - k]

            if (nums[i] + current_flips) % 2 == 0:
                if i + k > n:
                    return -1
                flip[i] = 1
                current_flips += 1
                result += 1

        return result


# solution - queue
from collections import deque
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        q = deque()
        res = 0

        for i in range(len(nums)):

            while q and i > q[0] + k - 1:
                q.popleft()

            if (nums[i] + len(q)) % 2 == 0:
                if i + k > len(nums):
                    return -1

                res += 1
                q.append(i)

        return res