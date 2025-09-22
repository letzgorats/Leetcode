# defaultdict solution
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = defaultdict(int)

        for n in nums:
            cnt[n] += 1

        value_list = sorted(cnt.values(),reverse=True)
        tmp = value_list[0]
        answer = tmp
        for v in value_list[1:]:

            if v == tmp:
                answer += v
            else:
                break

        return answer


# Counter solution

from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = Counter(nums)
        # print(cnt)
        cnt = sorted(cnt.items(),key=lambda x : x[1],reverse=True)
        largest = cnt[0][1]
        answer = 0

        for n,c in cnt:

            if c != largest :
                break
            else:
                answer += c

        return answer


# solution 3 - (max,greedy) - (3ms) - (2025.09.22)
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        counts = Counter(nums)

        # print(counts)

        max_v = 0
        ans = 0
        for k, v in counts.items():
            ans += v
            if max_v > v:
                ans -= v
            elif max_v == v:
                continue
            elif max_v < v:
                max_v = v
                ans = v

        return ans