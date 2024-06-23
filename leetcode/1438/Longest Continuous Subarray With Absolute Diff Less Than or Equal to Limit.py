# solution - two pointers + sliding window (monotonic queue)
from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # two pointers

        left, right = 0, 0
        answer = 0
        min_q, max_q = deque(), deque()

        for right in range(len(nums)):

            # 현재 값을 덱에 추가하며 최소값 덱 업데이트
            while min_q and nums[right] < nums[min_q[-1]]:
                min_q.pop()
            min_q.append(right)

            # 현재 값을 덱에 추가하며 최대값 덱 업데이트
            while max_q and nums[right] > nums[max_q[-1]]:
                max_q.pop()
            max_q.append(right)

            # 현재 윈도우의 최대값과 최소값의 차이가 limit를 초과하는지 확인
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                # 왼쪽 포인터를 이동하여 윈도우 축소
                left += 1

                # 왼쪽 포인터가 덱의 앞부분에 위치하면 덱에서 제거
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            # 현재 윈도우의 길이를 계산하여 최대값 업데이트
            answer = max(answer, right - left + 1)

        return answer
