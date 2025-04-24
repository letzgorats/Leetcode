# solution 1 - O(n^2) - (529ms) - (2025.04.24)
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        essential = set(nums)

        left, right = 0, 0
        answer = 0

        while right <= len(nums):

            if essential == set(nums[left:right]):
                # print(nums[left:right])
                answer += (len(nums) - right + 1)
                left += 1
                right = (left + 1)
            else:
                right += 1
                # print(answer)

        return answer

'''
slicing 하는 방법은 너무 무거운 방법
'''

# solution 2 - O(n), sliding window - (10ms) - (2025.04.24)
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        total_unique = len(set(nums))
        answer = 0
        freq = defaultdict(int)

        left = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) == total_unique:
                answer += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return answer
'''
전형적인 sliding window 템플릿
'''