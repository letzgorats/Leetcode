from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        if k > len(nums):
            return 0
        if k == 1:
            return max(nums)

        cur_sum = 0
        answer = 0
        freq = defaultdict(int)  # 요소의 빈도 관리

        for i in range(len(nums)):

            cur_sum += nums[i]
            freq[nums[i]] += 1

            # 윈도우 크기가 k를 초과하면, 맨 왼쪽 숫자 제거
            if i >= k:
                cur_sum -= nums[i - k]
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]] == 0:
                    del freq[nums[i - k]]

            # 중복이 없는 경우 최대값 경신
            if len(freq) == k:
                answer = max(answer, cur_sum)

        return answer