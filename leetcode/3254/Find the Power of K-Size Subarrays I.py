# solution 1 - greedy - O(n*k)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        answer = [-1] * (len(nums) - k + 1)

        for i in range(len(nums) - k + 1):
            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    break
            else:
                answer[i] = max(nums[i:i + k])

        return answer

# solution 2 - monotonic stack - O(n)
from collections import deque


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums

        n = len(nums)
        answer = []
        window = deque()

        for i in range(n):

            while window and i - window[0] >= k:
                window.popleft()

            if not window or nums[i] - nums[i - 1] == 1:
                window.append(i)

            else:
                window.clear()
                window.append(i)

            if i >= k - 1:
                answer.append(nums[i] if len(window) == k else -1)

        return answer