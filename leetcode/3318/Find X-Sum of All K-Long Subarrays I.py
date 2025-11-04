# solution 1 - (greedy,hash table) - (21ms) - (2025.11.04)
from collections import Counter
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        def cal(counts):

            tmp = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
            # print(tmp)

            # 가장 많이 나온 x 개의 숫자
            ans = 0
            for i in range(min(x, len(tmp))):
                ans += (tmp[i][0] * tmp[i][1])

            return ans

        answer = []
        cnts = Counter(nums[:k])

        answer.append(cal(cnts))
        left = 0
        for r in range(k, len(nums)):
            cnts[nums[r]] += 1
            cnts[nums[left]] = max(cnts[nums[left]] - 1, 0)
            answer.append(cal(cnts))
            left += 1

        # print(answer)
        return answer






