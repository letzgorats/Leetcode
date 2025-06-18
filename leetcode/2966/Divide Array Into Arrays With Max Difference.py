# solution 1 - (greedy) - (762ms) - (2024.02.01)
class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        nums = sorted(nums)
        answer = [nums[:3]]

        st = nums[0]
        for i in range(3,n,3):
            # print(i,answer)
            if (nums[i-1] - st) <= k:
                answer.append(nums[i:i+3])
                st = nums[i]
            else:
                return []

        if answer[-1][0] + k < answer[-1][2] :
            return []
        

        return answer

        

# solution 2 - (sort) - (74ms) - (2025.06.18)
from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        answer = []
        nums.sort()

        for i in range(0, len(nums), 3):

            if nums[i + 2] - nums[i] <= k:
                answer.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                answer = []
                break

        return answer

