from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        left = 0  # 윈도우의 시작점
        answer = 0

        min_q, max_q = deque(), deque()  # 최소값과 최대값의 인덱스를 저장하는 deque

        for right in range(len(nums)):  # 'right'는 윈도우의 끝점을 나타냄

            while min_q and nums[min_q[-1]] > nums[right]:
                min_q.pop()  # 현재 숫자보다 큰 값은 deque에서 제거
            min_q.append(right)  # 새로운 최소값 후보 추가

            while max_q and nums[max_q[-1]] < nums[right]:
                max_q.pop()  # 현재 숫자보다 작은 값은 deque에서 제거
            max_q.append(right)  # 새로운 최대값 후보 추가

            # check if max-min > 2, shrink the window
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1

                # Remove indices outside the window

                if min_q[0] < left:
                    min_q.popleft()  # 윈도우 밖에 있는 최소값 제거
                if max_q[0] < left:
                    max_q.popleft()  # 윈도우 밖에 있는 최대값 제거

            answer += right - left + 1

        return answer
